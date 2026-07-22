# Lesson 5.6 - Sets

## What is a Set?

A set is an unordered collection that stores only unique values.

Duplicate values are automatically removed.

Example

```python
numbers = {1, 2, 3, 2, 1}
```

Output

```
{1, 2, 3}
```

---

## Why Use Sets?

Sets are useful for:

- Removing duplicates
- Fast membership checking
- Comparing collections

---

## Creating a Set

```python
colors = {"Red", "Blue", "Green"}
```

---

## Empty Set

Wrong

```python
data = {}
```

Creates a dictionary.

Correct

```python
data = set()
```

---

## Add Items

```python
colors.add("Yellow")
```

---

## Remove Items

```python
colors.remove("Blue")
```

Raises an error if the item does not exist.

---

## discard()

```python
colors.discard("Blue")
```

Does not raise an error if the item is missing.

Preferred when you're unsure whether the item exists.

---

## Membership

```python
print("Python" in skills)
```

Returns

```
True
```

or

```
False
```

---

## Convert List to Set

```python
numbers = [1, 2, 2, 3, 4, 4]

unique_numbers = set(numbers)
```

Removes duplicates.

---

## Convert Set to List

```python
numbers = list(unique_numbers)
```

---

## Union

Returns all unique values.

```python
a | b
```

---

## Intersection

Returns common values.

```python
a & b
```

---

## Difference

Returns values present in one set but not the other.

```python
a - b
```

---

# List vs Set

| List | Set |
|------|------|
| Ordered | Unordered |
| Allows duplicates | Unique values only |
| Supports indexing | No indexing |
| Slower membership check | Faster membership check |

---

# Best Practices

- Use sets for unique data.
- Use sets for duplicate removal.
- Use sets for comparisons.
- Do not use sets when order matters.

---

# Common Mistakes

Wrong

```python
numbers = {}
```

Creates a dictionary.

Correct

```python
numbers = set()
```

---

Wrong

```python
skills[0]
```

Sets do not support indexing.

---

# Key Takeaways

- Sets store only unique values.
- Sets are unordered.
- Membership checking is very fast.
- Useful for removing duplicates.
- Main operations:
  - Union (`|`)
  - Intersection (`&`)
  - Difference (`-`)