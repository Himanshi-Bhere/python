# Lesson 5.5 - Tuples

## What is a Tuple?

A tuple is an ordered collection that cannot be modified after it is created.

Lists use

```python
[]
```

Tuples use

```python
()
```

Example

```python
student = ("Himanshi", 21, "EXTC")
```

---

## Why Tuples Exist

Some data should never change.

Examples

- Employee ID
- GPS Coordinates
- API Response
- Database Record ID
- RGB Color

Tuples protect such data from accidental modification.

---

## Creating Tuples

```python
colors = ("Red", "Blue", "Green")
```

```python
marks = (95, 88, 91)
```

Mixed values

```python
student = ("Himanshi", 21, 9.49)
```

---

## Accessing Values

Works exactly like lists.

```python
student[0]
```

Output

```
Himanshi
```

Negative indexing also works.

```python
student[-1]
```

---

## Length

```python
len(student)
```

Returns the number of items.

---

## Looping

```python
for item in student:
    print(item)
```

---

## Tuple Packing

Python automatically creates a tuple.

```python
person = "Himanshi", 21, "Mumbai"
```

Same as

```python
person = ("Himanshi", 21, "Mumbai")
```

---

## Tuple Unpacking

```python
name, age, city = person
```

Now

```python
print(name)
print(age)
print(city)
```

This is cleaner than indexing.

---

## Immutable

Tuples cannot be modified.

Wrong

```python
student[0] = "Rahul"
```

Output

```
TypeError
```

Reason

Tuples are immutable.

---

## One Item Tuple

Wrong

```python
marks = (90)
```

This is an integer.

Correct

```python
marks = (90,)
```

The comma makes it a tuple.

---

## Tuple vs List

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| [] | () |
| Can add/remove items | Cannot modify |
| Used for changing data | Used for fixed data |

---

## Best Practices

- Use tuples for fixed values.
- Use lists for changing collections.
- Use tuple unpacking whenever possible.
- Use tuples for coordinates, IDs and API responses.

---

## Common Mistakes

❌

```python
marks = (95)
```

Correct

```python
marks = (95,)
```

---

❌

Trying to modify a tuple.

```python
student[0] = "Rahul"
```

Raises

```
TypeError
```

---

# Key Takeaways

- Tuples are ordered collections.
- Tuples are immutable.
- Access values using indexes.
- Packing creates tuples automatically.
- Unpacking assigns tuple values to multiple variables.
- Tuples are commonly used for fixed data.