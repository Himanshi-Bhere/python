# File Modes in Python

File modes define how a file is opened and what operations are allowed.

---

## "r" (Read)

- Opens an existing file for reading.
- Raises FileNotFoundError if the file does not exist.
- Does not modify the file.

Example

```python
with open("data.txt", "r") as file:
    print(file.read())
```

---

## "w" (Write)

- Opens a file for writing.
- Creates the file if it does not exist.
- Deletes all existing content before writing.

Example

```python
with open("report.txt", "w") as file:
    file.write("New Report")
```

---

## "a" (Append)

- Opens a file for appending.
- Creates the file if it does not exist.
- Preserves existing content.
- New data is written at the end.

Example

```python
with open("log.txt", "a") as file:
    file.write("Server Started\n")
```

---

## "r+" (Read + Write)

- Opens an existing file.
- Allows reading and writing.
- Does not create a new file.
- File pointer starts at the beginning.

---

## "w+" (Write + Read)

- Creates a new file if needed.
- Deletes existing content.
- Allows both reading and writing.

---

## "a+" (Append + Read)

- Creates the file if it does not exist.
- Allows reading and appending.
- New data is always written at the end.

---

## Summary

| Mode | Read | Write | Create File | Deletes Existing Data |
|------|------|------|-------------|-----------------------|
| r | ✅ | ❌ | ❌ | ❌ |
| w | ❌ | ✅ | ✅ | ✅ |
| a | ❌ | ✅ | ✅ | ❌ |
| r+ | ✅ | ✅ | ❌ | ❌ |
| w+ | ✅ | ✅ | ✅ | ✅ |
| a+ | ✅ | ✅ | ✅ | ❌ |

---

## When to Use

r

- Read configuration files
- Read reports
- Read datasets

w

- Generate reports
- Export data
- Save fresh files

a

- Chat history
- Logs
- Audit records
- Attendance systems
- Banking transactions

---

## Industry Rule

Choose the correct file mode before writing code.

Using `"w"` instead of `"a"` can permanently erase production data.