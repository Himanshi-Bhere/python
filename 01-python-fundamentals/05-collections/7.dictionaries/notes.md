# Lesson 5.7 - Dictionaries (Part 1)

## What is a Dictionary?

A dictionary stores data as **key-value pairs**.

Example

```python
employee = {
    "name": "Himanshi",
    "role": "Cloud Engineer",
    "salary": 85000
}
```

---

## Why Use Dictionaries?

Instead of remembering indexes

```python
employee[2]
```

Use meaningful keys

```python
employee["salary"]
```

This makes code easier to read and maintain.

---

## Dictionary Syntax

```python
student = {
    "name": "Rahul",
    "age": 20,
    "city": "Mumbai"
}
```

---

## Access Values

```python
print(student["name"])
```

---

## Update Values

```python
student["age"] = 21
```

---

## Add New Key

```python
student["college"] = "KCCEMSR"
```

---

## Delete Key

```python
del student["city"]
```

---

## Rules

Keys must be unique.

```python
student = {
    "name": "Rahul",
    "name": "Amit"
}
```

Only the last value is kept.

---

Values can be of any type.

```python
student = {
    "name": "Himanshi",
    "age": 21,
    "skills": ["Python", "Linux"],
    "placed": False
}
```

---

## List vs Dictionary

| List | Dictionary |
|------|------------|
| Uses indexes | Uses keys |
| Ordered | Ordered (Python 3.7+) |
| Access by position | Access by key |
| Good for sequences | Good for records |

---

## Best Practices

- Use meaningful key names.
- Keep keys consistent.
- Use dictionaries for structured data.
- Prefer f-strings while printing values.

---

## Common Mistakes

Wrong

```python
employee[0]
```

Correct

```python
employee["name"]
```

---

Wrong

```python
employee["salary"] = "85000"
```

Store numbers as numbers whenever possible.

```python
employee["salary"] = 85000
```

---

## Key Takeaways

- Dictionaries store key-value pairs.
- Keys are unique.
- Values can be any data type.
- Add using `dict[key] = value`.
- Update using `dict[key] = new_value`.
- Delete using `del dict[key]`.