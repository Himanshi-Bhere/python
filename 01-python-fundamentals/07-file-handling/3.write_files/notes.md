# Writing Files in Python

## write()

- Used to write data into a file.
- Accepts only strings.
- Returns the number of characters written.

Syntax

```python
file.write(data)
```

---

## Write Mode (`"w"`)

```python
file = open("report.txt", "w")
```

- Creates the file if it does not exist.
- If the file already exists, all previous content is deleted (overwritten).

---

## Writing One Line

```python
file.write("Hello World")
```

Contents of the file

```
Hello World
```

---

## Writing Multiple Lines

Use `\n` to move to the next line.

Example

```python
file.write("Line 1\n")
file.write("Line 2\n")
file.write("Line 3")
```

Output

```
Line 1
Line 2
Line 3
```

---

## Return Value

```python
count = file.write("Python")
print(count)
```

Output

```
6
```

Because `"Python"` contains 6 characters.

---

## Best Practices

- Always close the file after writing.
- Use `\n` to create new lines.
- Remember that `"w"` deletes all previous content before writing.
- Store long text in a variable before writing if it improves readability.