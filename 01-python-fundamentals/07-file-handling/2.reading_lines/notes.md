# Reading Files in Python

## read()

- Reads the entire file.
- Returns a string.
- Suitable for small files.

Example

```python
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()
```

---

## read(number)

- Reads a specific number of characters.
- Returns a string.

Example

```python
print(file.read(7))
```

Output

```
Welcome
```

---

## readline()

- Reads only one line.
- Returns a string.
- Automatically moves the file pointer to the next line.

Example

```python
print(file.readline())
print(file.readline())
```

Output

```
Himanshi
Rahul
```

---

## readlines()

- Reads all lines.
- Returns a list.
- Each line becomes one element in the list.

Example

```python
lines = file.readlines()
```

Output

```python
[
'Himanshi\n',
'Rahul\n',
'Sara\n',
'Amit'
]
```

---

## Removing Newline Characters

Use

```python
strip()
```

Example

```python
for line in lines:
    print(line.strip())
```

---

## Difference

| Method | Returns | Best Use |
|---------|----------|----------|
| read() | String | Entire file |
| read(number) | String | Fixed characters |
| readline() | String | One line |
| readlines() | List | All lines |

---

## Best Practices

- Always close the file using `file.close()`.
- Use `readline()` for very large files.
- Use `readlines()` when list operations are required.
- Use `strip()` to remove newline characters while printing.