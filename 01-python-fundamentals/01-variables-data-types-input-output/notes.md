# 📘 Lesson 1: Variables, Data Types, Input & Output

## 1. Variables

A **variable** stores a value in memory.

```python
student_name = "Himanshi"
student_age = 21
```

**Best Practice:** Use meaningful names and follow **snake_case**.

✅ Good

```python
student_name
employee_id
account_balance
```

❌ Bad

```python
x
a
abc
```

---

## 2. Basic Data Types

| Data Type | Purpose             | Example             |
| --------- | ------------------- | ------------------- |
| `int`     | Whole numbers       | `age = 21`          |
| `float`   | Decimal numbers     | `cgpa = 9.49`       |
| `str`     | Text                | `name = "Himanshi"` |
| `bool`    | True / False values | `is_student = True` |

Check a variable's type:

```python
print(type(age))
```

---

## 3. User Input

Take input using `input()`.

```python
name = input("Enter your name: ")
```

> **Remember:** `input()` always returns a **string (`str`)**.

---

## 4. Type Conversion

Convert data when needed.

```python
age = int(input("Enter age: "))
cgpa = float(input("Enter CGPA: "))
```

Common conversions:

```python
int("25")
float("9.5")
str(100)
```

---

## 5. Output (Printing)

Use **f-strings** for clean and readable output.

```python
print(f"Hello, {name}")
```

---

## 6. Comments

Single-line comment

```python
# This is a comment
```

Multi-line comment

```python
"""
Multiple line comment
"""
```

---

# Common Mistakes

❌ Forgetting type conversion

```python
age = input()
```

✅ Correct

```python
age = int(input())
```

---

❌ Poor variable names

```python
a = 10
```

✅ Better

```python
student_age = 10
```

---

# Quick Revision

* Variable = Stores a value.
* Main data types = `int`, `float`, `str`, `bool`.
* `input()` always returns a **string**.
* Use `int()` or `float()` when numerical input is needed.
* Use **f-strings** for printing.
* Follow **snake_case** naming.
* Write clean, readable code.
