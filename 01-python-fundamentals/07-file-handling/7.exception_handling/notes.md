# Exception Handling in File Handling

## Why Exception Handling?

Exception handling prevents programs from crashing when unexpected errors occur.

Instead of terminating, the program handles the error gracefully.

---

## Syntax

```python
try:
    risky code

except SomeError:
    handle error

finally:
    cleanup code
```

---

## try

- Contains code that may produce an exception.
- If no error occurs, the program continues normally.

---

## except

- Executes only when an exception occurs.
- Different exceptions can have different handlers.

Example

```python
except FileNotFoundError:
    print("File not found")
```

---

## finally

- Always executes.
- Runs whether an exception occurs or not.
- Used for cleanup operations.

Example

```python
finally:
    print("Program Finished")
```

---

## Common File Exceptions

| Exception | Description |
|------------|-------------|
| FileNotFoundError | File does not exist |
| PermissionError | No permission to access the file |
| IsADirectoryError | Attempted to open a directory as a file |
| OSError | General operating system error |
| Exception | Handles unexpected exceptions |

---

## Benefits

- Prevents application crashes
- Improves user experience
- Makes software reliable
- Allows graceful recovery
- Helps with debugging

---

## Industry Uses

- Banking software
- Hospital systems
- Payroll systems
- Automation scripts
- API servers
- Desktop applications
- AI pipelines