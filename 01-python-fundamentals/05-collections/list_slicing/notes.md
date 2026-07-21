# Lesson 5.3 - List Slicing

## What is Slicing?

Slicing means extracting a portion of a list.

Instead of accessing one item, slicing returns multiple items.

---

## Syntax

```python
list[start:stop]
```

- Start index is included.
- Stop index is excluded.

---

## Example

```python
numbers = [10, 20, 30, 40, 50]
```

```python
numbers[1:4]
```

Output

```
[20, 30, 40]
```

---

## From Beginning

```python
numbers[:3]
```

Output

```
[10, 20, 30]
```

---

## Till End

```python
numbers[2:]
```

Output

```
[30, 40, 50]
```

---

## Entire List

```python
numbers[:]
```

Returns a shallow copy of the list.

---

## Negative Slicing

```python
numbers[-2:]
```

Output

```
[40, 50]
```

Useful for accessing recent items.

---

## Step

Syntax

```python
list[start:stop:step]
```

Example

```python
numbers[::2]
```

Output

```
[10, 30, 50]
```

Skips every second element.

---

## Reverse Using Slicing

```python
numbers[::-1]
```

Output

```
[50, 40, 30, 20, 10]
```

Creates a reversed copy.

---

## Copy Using Slicing

```python
copy_numbers = numbers[:]
```

Changes made to the copied list do not affect the original.

---

# Difference

Reverse copy

```python
numbers[::-1]
```

Original list remains unchanged.

---

Reverse method

```python
numbers.reverse()
```

Original list changes.

---

# Best Practices

- Use slicing to extract portions of a list.
- Remember the stop index is excluded.
- Use negative slicing for recent elements.
- Use `[::-1]` when you need a reversed copy.
- Use `[:]` or `.copy()` to create an independent copy.

---

# Common Mistakes

❌

```python
numbers[1:4]
```

Thinking index 4 is included.

It is **not**.

---

❌

```python
copy = original
```

Both variables point to the same list.

Use

```python
copy = original.copy()
```

or

```python
copy = original[:]
```

---

# Key Takeaways

- Slicing extracts part of a list.
- Syntax: `list[start:stop:step]`
- Stop index is excluded.
- Negative indexes work with slicing.
- `[::-1]` creates a reversed copy.
- `[:]` creates a shallow copy.