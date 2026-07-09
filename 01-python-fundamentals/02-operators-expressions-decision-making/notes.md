# Lesson 2 - Operators, Expressions & Decision Making

## 1. Arithmetic Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| + | Addition | 10 + 5 |
| - | Subtraction | 10 - 5 |
| * | Multiplication | 10 * 5 |
| / | Division | 10 / 5 |
| // | Floor Division | 10 // 3 |
| % | Modulus (Remainder) | 10 % 3 |
| ** | Power | 2 ** 3 |

---

## 2. Comparison Operators

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not Equal |
| > | Greater than |
| < | Less than |
| >= | Greater than or Equal |
| <= | Less than or Equal |

Comparison operators always return **True** or **False**.

Example:

```python
age = 20

print(age >= 18)   # True
```

---

## 3. Logical Operators

### and

Returns True if **both conditions are True**.

```python
age >= 18 and citizen
```

---

### or

Returns True if **at least one condition is True**.

```python
age >= 18 or citizen
```

---

### not

Reverses a Boolean value.

```python
is_logged_in = False

print(not is_logged_in)
```

---

## 4. Assignment Operators

```python
x += 5
x -= 5
x *= 2
x /= 2
```

Shortcut for updating variables.

---

## 5. Expressions

An expression is any piece of code that produces a value.

Examples:

```python
10 + 5

age >= 18

num1 * num2
```

---

## 6. if Statement

Runs code only if the condition is True.

```python
if age >= 18:
    print("Adult")
```

---

## 7. if-else

Choose between two outcomes.

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## 8. if-elif-else

Checks multiple conditions.

```python
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
else:
    print("Fail")
```

---

## Best Practices

- Use meaningful variable names.
- Keep conditions simple.
- Use `.lower()` when comparing user input.
- Keep indentation consistent (4 spaces).
- Use chained comparisons when possible (`90 <= marks <= 100`).

---

## Common Mistakes

❌ Using `=` instead of `==`

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

---

❌ Comparing a string with a number.

```python
age = input()
```

Correct:

```python
age = int(input())
```

---

## Key Takeaways

- Operators perform operations on values.
- Comparison operators return True or False.
- Logical operators combine conditions.
- `if`, `elif`, and `else` control program flow.
- Conditions decide which block of code executes.