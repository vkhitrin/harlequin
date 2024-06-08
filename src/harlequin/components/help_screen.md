### General Bindings

- ctrl+q: Quit Harlequin
- F1: Show this screen.
- F2: Focus on the Query Editor.
- F5: Focus on the Results Viewer.
- F6: Focus on the Data Catalog.
- F8: Show the Query History Viewer.
- F9, ctrl+b: Toggle the sidebar.
- F10: Toggle full screen mode for the current widget.
- F12: Open Adapter Details screen.
- ctrl+e: Write the returned data to a CSV, Parquet, or JSON file.
- ctrl+r: Refresh the Data Catalog.


### Query Editor Bindings

#### Actions

- F4: Format the query.
- ctrl+enter, ctrl+j: Run the query.

- ctrl+o: Open a text file in the Query Editor.
- ctrl+s: Save the contents of the Query Editor to a file.

- ctrl+n: Create a new buffer (editor tab).
- ctrl+w: Close the current buffer (editor tab).
- ctrl+k: View the next buffer (editor tab).

- ctrl+g: Go to line
- ctrl+f: Find
- F3: Find next (like Find, but uses previous value).

#### Editing Text

- ctrl+a: Select all, move the cursor to the end of the query.
- ctrl+x: Cut selected text.
- ctrl+c: Copy selected text.
- ctrl+v, ctrl+u, shift+insert: Paste selected text.
- ctrl+z: Undo.
- ctrl+y: Redo.
- ctrl+/, ctrl+_: Toggle comments on selected line(s).
- tab: Insert spaces at cursor to move the cursor to the next tab stop, or indent the selected line(s) to the next tab stop.
- shift+tab: Dedent the selected line(s) to the next tab stop.
- shift+delete: Delete the current line.

#### Using Autocomplete

*With the autocomplete list open:*
- up,down,PgUp,PgDn: Select a different item in the list.
- tab,enter: Place the current selection in the Query Editor.
- escape: Dismiss the autocomplete list.

#### Moving the Cursor

- up,down,left,right: Move the cursor one position.
- home: Move the cursor to the start of the line.
- end: Move the cursor to the end of the line.
- ctrl+home: Move the cursor to the start of the query.
- ctrl+end: Move the cursor to the end of the query.
- PgUp: Move the cursor up one screen.
- PgDn: Move the cursor down one screen.
- ctrl+up: Scroll up one line.
- ctrl+down: Scroll down one line.
- ctrl+left: Move the cursor to the start of the current token.
- ctrl+right: Move the cursor to the end of the current token.
- shift+[any]: Select text while moving the cursor.


### Results Viewer Bindings

- ctrl+c: Copy selected data to the clipboard.

#### Switching Tabs

- j: Switch to the previous tab.
- k: Switch to the next tab.

#### Moving the Cursor

- up,down,left,right: Move the cursor one cell.
- tab: Move the cursor to the next cell in the table.
- shift+tab: Move the cursor to the previous cell in the table.
- home, ctrl+up: Move the cursor to the top of the current column.
- end, ctrl+down: Move the cursor to the bottom of the current column.
- ctrl+left: Move the cursor to the start of the current row.
- ctrl+right: Move the cursor to the end of the current row.
- ctrl+home: Move the cursor to the start of the table.
- ctrl+end: Move the cursor to the end of the table.
- PgUp: Move the cursor up one screen.
- PgDn: Move the cursor down one screen.
- shift+[any]: Select range while moving the cursor.


### Data Catalog Bindings

- ctrl+enter, ctrl+j: Insert the current name into the Query Editor.
- ctrl+c: Copy the current name to the clipboard.

#### Switching Tabs

- j: Switch to the previous tab.
- k: Switch to the next tab.

#### Moving the Cursor

- up,down: Move the cursor one row.
- enter,space: Toggle the expand/collapsed state of the current item.

### Query History Viewer Bindings

- up,down,PgUp,PgDn: Change selection and scroll.
- tab: Change focus between the history list and the query preview pane.
- enter: Create a new Editor buffer and insert the highlighted query.
- escape: Return to the main screen.
