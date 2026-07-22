# Lesson 5.2 - List Methods

## Why List Methods?

Lists are not only used to store data.

They also allow us to:

- Add items
- Remove items
- Search items
- Sort items
- Reverse items
- Copy items

These operations are performed using list methods.

---

## append()

Adds an item to the end of the list.

```python
tasks = ["Read", "Clean"]

tasks.append("Send")
```

Result

```python
["Read", "Clean", "Send"]
```

---

## insert()

Adds an item at a specific position.

```python
tasks.insert(1, "Validate")
```

Result

```python
["Read", "Validate", "Clean", "Send"]
```

---

## remove()

Removes an item by value.

```python
tasks.remove("Clean")
```

Result

```python
["Read", "Send"]
```

Raises `ValueError` if the item doesn't exist.

---

## pop()

Removes an item by index.

```python
tasks.pop(1)
```

If no index is given,

```python
tasks.pop()
```

removes the last item.

---

## index()

Returns the position of an item.

```python
tasks.index("Send")
```

Output

```
2
```

---

## count()

Counts occurrences.

```python
tasks.count("Testing")
```

Output

```
2
```

---

## sort()

Sorts the list in ascending order.

```python
numbers.sort()
```

Result

```
[1, 2, 5, 8]
```

---

## reverse()

Reverses the list.

```python
numbers.reverse()
```

Result

```
[8, 5, 2, 1]
```

---

## copy()

Creates an independent copy.

```python
copy_tasks = tasks.copy()
```

Changes made to the copied list do not affect the original.

---

# Important

These methods modify the original list:

- append()
- insert()
- remove()
- pop()
- sort()
- reverse()

They return **None**.

Do NOT write

```python
tasks = tasks.sort()
```

Correct

```python
tasks.sort()
```

---

# Best Practices

- Use `append()` to add at the end.
- Use `insert()` when order matters.
- Use `remove()` to delete by value.
- Use `pop()` to delete by index.
- Use `copy()` before modifying a list that should remain unchanged.
- Prefer `enumerate()` instead of manually tracking indexes.

---

# Common Mistakes

❌

```python
print(tasks.append("A"))
```

Output

```
None
```

Correct

```python
tasks.append("A")
print(tasks)
```

---

❌

```python
tasks = tasks.sort()
```

Correct

```python
tasks.sort()
```

---

# Key Takeaways

- Lists are mutable.
- List methods modify the original list.
- `copy()` creates an independent list.
- `count()` returns occurrences.
- `index()` returns the position of an item.
- `sort()` sorts data.
- `reverse()` reverses data.