# Lesson 5.4 - Nested Lists

## What is a Nested List?

A nested list is a list that contains one or more lists.

Example

```python
students = [
    ["Himanshi", 21, "EXTC"],
    ["Rahul", 22, "Computer"],
    ["Sara", 20, "IT"]
]
```

Each inner list represents one record.

---

## Why Use Nested Lists?

Nested lists help store structured data like tables.

Example

| Name | Age | Branch |
|------|-----|---------|
| Himanshi | 21 | EXTC |
| Rahul | 22 | Computer |
| Sara | 20 | IT |

---

## Accessing Records

First student

```python
students[0]
```

Output

```
["Himanshi", 21, "EXTC"]
```

---

## Accessing Individual Values

Name

```python
students[0][0]
```

Age

```python
students[0][1]
```

Branch

```python
students[0][2]
```

---

## Updating Values

```python
students[1][2] = "AI & DS"
```

Updates Rahul's branch.

---

## Adding Records

```python
students.append(["Alex", 23, "Cyber Security"])
```

Adds a new student.

---

## Looping Through Nested Lists

```python
for student in students:
    print(student)
```

---

Access individual values

```python
for student in students:
    print(student[0])
```

Prints only names.

---

## Example

```python
employees = [
    ["E101", "Himanshi", "Cloud Engineer", 85000],
    ["E102", "Rahul", "Backend Developer", 78000]
]
```

Employee Name

```python
employee[1]
```

Salary

```python
employee[3]
```

---

# Advantages

- Stores structured data.
- Easy to loop through.
- Good for table-like data.

---

# Limitations

Reading

```python
student[2]
```

doesn't tell what value it represents.

You must remember the position.

This is why dictionaries are usually preferred in real projects.

---

# Best Practices

- Keep the order of values consistent.
- Use nested lists for simple tabular data.
- Avoid deeply nested lists.
- Use loops instead of writing repeated code.

---

# Common Mistakes

❌ Wrong

```python
students[1]
```

Returns the whole second record.

---

To access the student's name

```python
students[1][0]
```

---

# Key Takeaways

- A nested list is a list inside another list.
- Each inner list usually represents one record.
- Access values using two indexes.
- Nested lists work well for tabular data.
- Dictionaries are often a better choice for readability.