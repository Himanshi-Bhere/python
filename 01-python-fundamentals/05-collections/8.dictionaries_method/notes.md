# Dictionary Methods

Dictionary methods help us safely access, update, remove, and process dictionary data.

---

## 1. get()

Safely gets a value using its key.

```python
user = {
    "name": "Himanshi",
    "role": "Cloud Engineer"
}

print(user.get("name"))
```

Output:

```text
Himanshi
```

We can provide a default value if the key does not exist:

```python
print(user.get("salary", 0))
```

Output:

```text
0
```

### Why use get()?

This can cause a `KeyError`:

```python
user["salary"]
```

This is safer:

```python
user.get("salary")
```

---

## 2. keys()

Returns all dictionary keys.

```python
print(user.keys())
```

Example output:

```text
dict_keys(['name', 'role'])
```

---

## 3. values()

Returns all dictionary values.

```python
print(user.values())
```

Example:

```text
dict_values(['Himanshi', 'Cloud Engineer'])
```

---

## 4. items()

Returns key-value pairs.

```python
print(user.items())
```

Most commonly used with a loop:

```python
for key, value in user.items():
    print(f"{key}: {value}")
```

---

## 5. update()

Updates existing values or adds new key-value pairs.

```python
user.update({
    "city": "Mumbai",
    "salary": 90000
})
```

If the key already exists → its value is updated.

If the key does not exist → a new key is created.

---

## 6. pop()

Removes a key and returns its value.

```python
role = user.pop("role")

print(role)
```

A safer version is:

```python
user.pop("role", None)
```

This avoids a `KeyError` if the key does not exist.

---

## 7. copy()

Creates a copy of a dictionary.

```python
backup_user = user.copy()
```

Now:

```python
backup_user["name"] = "Rahul"
```

does not change the original dictionary's `"name"`.

Note: `copy()` creates a shallow copy. We will understand shallow vs deep copying later when it becomes relevant.

---

# Important Pattern

A very common Python pattern is:

```python
for key, value in data.items():
    print(key, value)
```

Use:

- `get()` → safely access a value
- `keys()` → access keys
- `values()` → access values
- `items()` → access keys and values
- `update()` → update/add data
- `pop()` → remove data
- `copy()` → copy a dictionary

---

# Best Practices

- Use `get()` when a key may not exist.
- Use `items()` when looping through both keys and values.
- Use `update()` when changing multiple fields.
- Store numbers as numbers, not strings.
- Use meaningful dictionary keys.
- Use `copy()` when you need a separate dictionary.

---

# Common Mistake

Avoid:

```python
salary = "90000"
```

when the value represents a number.

Prefer:

```python
salary = 90000
```

This allows calculations such as:

```python
salary + 5000
```