from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Sequence

from textual_fastdatatable.backend import AutoBackendType

from harlequin.catalog import Catalog
from harlequin.export_options import (
    ExportOptions,
)
from harlequin.options import HarlequinAdapterOption, HarlequinCopyOption


class HarlequinCursor(ABC):
    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def columns(self) -> list[tuple[str, str]]:
        """
        Gets a list of columns for the result set of the cursor.

        Returns: list[tuple[str, str]], where each tuple is the (name, type) of
            a column, where type should be a short (1-3 character) string. The
            columns must be ordered in the same order as the data returned by
            fetchall()
        """
        pass

    @abstractmethod
    def set_limit(self, limit: int) -> "HarlequinCursor":
        """
        Limits the number of results for future calls to fetchall().

        Args:
            limit (int): The maximum number of records to be returned
            by future calls to fetchall().

        Returns: HarlequinCursor, either a reference to self or a new
            cursor with the limit applied.
        """
        pass

    @abstractmethod
    def fetchall(self) -> AutoBackendType:
        """
        Returns data from the cursor's result set. Can return any type supported
        by textual-fastdatatable.

        Returns:
            pyarrow.Table |
            pyarrow.Record Batch |
            Sequence[Iterable[Any]] |
            Mapping[str, Sequence[Any]]
        """
        pass


class HarlequinConnection(ABC):
    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def execute(self, query: str) -> HarlequinCursor | None:
        """
        Executes query and returns a cursor (for a select stmt) or None. Raises
        HarlequinQueryError if the database raises an error in response to the query.

        Args:
            query (str): The text of a single query to execute

        Returns: HarlequinCursor | None

        Raises: HarlequinQueryError
        """
        pass

    @abstractmethod
    def get_catalog(self) -> Catalog:
        """
        Introspects the connected database and returns a Catalog object with
        items for each database, schema, table, view, column, etc.

        Returns: Catalog
        """
        pass

    def copy(self, query: str, path: Path, options: ExportOptions) -> None:
        """
        Exports data returned by query to a file or directory at path, using
        options.
        Args:
            query (str): The text of the query (select stmt) to be executed.
            path (Path): The destination location for the file(s) to be written.
            options (HarlequinCopyOptions): An instance of copy options specific to
                this operation and adapter.

        Returns: None

        Raises:
            NotImplementedError if the adapter does not have copy functionality.
            HarlequinCopyError for all other exceptions during export.
        """
        raise NotImplementedError

    def validate_sql(self, text: str) -> str:
        """
        Parses text as one or more queries; returns text if parsing does not result
        in an error; otherwise returns the empty string ("").

        Args:
            text (str): The text, which may compose one or more queries and partial
                queries.

        Returns: str, either the original text or the empty string ("")

        Raises: NotImplementedError if the adapter does not provide this optional
            functionality.
        """
        raise NotImplementedError


class HarlequinAdapter(ABC):
    """
    A HarlequinAdapter is the main abstraction for a database backend for
    Harlequin.

    It must declare its configuration setting the ADAPTER_OPTIONS
    class variable. If the adapter supports copying (exporting
    data to a file or directory), it also must declare COPY_OPTIONS.

    Adapters are initialized with a conn_str, a tuple of strings, and
    kwargs that represent CLI options. Adapters must be robust to receiving
    both subsets and supersets of their defined options as kwargs. They should
    disregard any extra (unexpected) kwargs.
    """

    ADAPTER_OPTIONS: list[HarlequinAdapterOption] | None = None
    COPY_OPTIONS: list[HarlequinCopyOption] | None = None

    @abstractmethod
    def __init__(self, conn_str: Sequence[str], **options: Any) -> None:
        """
        Initialize an adapter.

        Args:
            - conn_str (Sequence[str]): One or more connection strings. May be empty.
            - **options (Any): Options received from the command line, config file,
                or env variables. Adapters should be robust to receiving both subsets
                and supersets of their declared options. They should disregard any
                extra (unexpected) kwargs.
        """
        pass

    @abstractmethod
    def connect(self) -> tuple[HarlequinConnection, str]:
        """
        Creates and returns an initialized connection to a database. Necessary config
        should be stored in the HarlequinAdapter instance when it is created.

        Returns: tuple[HarlequinConnection, str], where the str is a message that
            will be passed to the user in a notification. If str is the empty string,
            no notification will be presented to the user.

        Raises: HarlequinConnectionError if a connection could not be established.
        """
        pass

    @property
    def implements_copy(self) -> bool:
        """
        True if the adapter's connection implements the copy() method. Adapter must
        also provide options for customizing the Export dialog GUI.
        """
        return self.COPY_OPTIONS is not None