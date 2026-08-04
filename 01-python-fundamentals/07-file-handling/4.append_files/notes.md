# Append Mode ("a")

Append mode is used to add new data to the end of a file without deleting its existing content.

Syntax:

file = open("filename.txt", "a")

Important Points:

- Opens the file in append mode.
- Existing data is preserved.
- New data is written at the end of the file.
- Creates the file automatically if it does not exist.
- File pointer starts at the end of the file.

Example:

file = open("log.txt", "a")

file.write("Server Started\n")

file.close()

Difference between "w" and "a"

"w"

- Deletes old content.
- Writes from the beginning.

"a"

- Keeps old content.
- Adds new content at the end.

Common Uses

- Application logs
- Chat history
- Visitor records
- Attendance systems
- Audit logs