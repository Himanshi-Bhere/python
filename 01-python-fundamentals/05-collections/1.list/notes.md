# Lesson 5 - Lists

## What is a List?

A list is an ordered, mutable collection that stores multiple values in a single variable.

Example:

```python
tasks = ["Read CSV", "Generate PDF", "Send Email"]
```

---

## Why Use Lists?

Without a list:

```python
task1 = "Read CSV"
task2 = "Generate PDF"
task3 = "Send Email"
```

With a list:

```python
tasks = [
    "Read CSV",
    "Generate PDF",
    "Send Email"
]
```

Lists make data easier to manage.

---

## Characteristics

- Ordered
- Mutable (can be modified)
- Allows duplicate values
- Can store different data types

---

## Creating a List

```python
numbers = [10, 20, 30]

names = ["A", "B", "C"]

mixed = ["Python", 21, True]
```

---

## Indexing

Lists start from index **0**.

```python
tasks = ["Read", "Clean", "Send"]

print(tasks[0])
```

Output:

```
Read
```

---

## Negative Indexing

```python
print(tasks[-1])
```

Output:

```
Send
```

Useful when you need the last item.

---

## Common Functions

Length

```python
len(tasks)
```

Output

```
3
```

---

## append()

Adds a new item at the end.

```python
tasks.append("Archive")
```

Result

```python
["Read", "Clean", "Send", "Archive"]
```

---

## enumerate()

Returns both index and value.

```python
for index, task in enumerate(tasks, start=1):
    print(index, task)
```

Output

```
1 Read
2 Clean
3 Send
```

---

# Best Practices

- Use meaningful variable names.
- Store related data together.
- Use plural variable names for lists.
- Use `enumerate()` instead of manually counting.
- Use negative indexing when accessing the last element.

---

# Common Mistakes

❌

```python
print(tasks[5])
```

IndexError if the index doesn't exist.

---

❌

```python
task = ["A", "B", "C"]
```

Prefer

```python
tasks = ["A", "B", "C"]
```

because it stores multiple items.

---

# Key Takeaways

- Lists store multiple values.
- Lists are ordered.
- Lists are mutable.
- Indexing starts at 0.
- Negative indexing starts from the end.
- `append()` adds items.
- `len()` returns the number of items.
- `enumerate()` returns both index and value.