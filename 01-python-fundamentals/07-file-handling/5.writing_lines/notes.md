# writelines()

`writelines()` writes multiple strings from a list (or any iterable) into a file.

Syntax

```python
file.writelines(list_of_strings)
```

Example

```python
students = [
    "Himanshi\n",
    "Rahul\n",
    "Sara\n"
]

file = open("students.txt", "w")
file.writelines(students)
file.close()
```

Output

Himanshi
Rahul
Sara

---

## Important

`writelines()` does NOT automatically add a newline (`\n`).

Wrong

```python
students = [
    "Himanshi",
    "Rahul",
    "Sara"
]
```

Output

```
HimanshiRahulSara
```

Correct

```python
students = [
    "Himanshi\n",
    "Rahul\n",
    "Sara\n"
]
```

---

## Difference Between write() and writelines()

### write()

- Writes one string at a time.
- Needs multiple calls to write multiple lines.

Example

```python
file.write("Rahul\n")
file.write("Sara\n")
```

### writelines()

- Writes all strings from a list in one call.
- Faster and cleaner when writing many lines.

Example

```python
names = [
    "Rahul\n",
    "Sara\n"
]

file.writelines(names)
```

---

## Common Uses

- Export employee lists
- Save cloud server names
- Generate reports
- Create configuration files
- Store log entries