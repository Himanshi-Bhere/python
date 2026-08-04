# File Handling – Reading Files

## What is File Handling?

File handling allows Python programs to read, write, update, and manage files stored on a computer. It is one of the most important skills for backend development, cloud engineering, automation, and data processing.

---

## Why is File Handling Important?

Almost every real-world application works with files.

Examples:
- Reading server logs
- Saving reports
- Processing CSV data
- Reading configuration files
- Managing JSON APIs
- Storing application data

---

## Opening a File

```python
file = open("server.log", "r")
```

- `"r"` means **read mode**.
- The file must already exist.

---

## Reading the Entire File

```python
content = file.read()
print(content)
```

Reads the complete contents as one string.

---

## Splitting into Lines

```python
lines = content.splitlines()
```

Creates a list where each line becomes one element.

Example:

```python
[
    "INFO Server Started",
    "ERROR Connection Lost"
]
```

---

## Counting Lines

```python
len(lines)
```

Returns the total number of log entries.

---

## Searching Text

```python
"ERROR" in content
```

Returns:

- True
- False

---

## Loop Through Every Line

```python
for line in lines:
    print(line)
```

Useful for processing logs one by one.

---

## Closing a File

```python
file.close()
```

Always close a file after reading it to free system resources.

---

## Key Functions

| Function | Purpose |
|----------|---------|
| open() | Opens a file |
| read() | Reads the whole file |
| splitlines() | Splits text into lines |
| len() | Counts items |
| in | Searches text |
| close() | Closes the file |

---

## Industry Applications

- Cloud Monitoring
- Log Analysis
- Automation Scripts
- DevOps Tools
- Security Monitoring
- Backend Applications

---

## Skills Learned

- Reading text files
- Processing log files
- Searching file contents
- Counting records
- Looping through file data
- Basic log analysis