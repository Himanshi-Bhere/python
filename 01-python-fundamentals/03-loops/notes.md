# Lesson 3 - Loops

## Why Loops?

Loops repeat a block of code without writing it multiple times.

---

## while Loop

Runs as long as the condition is True.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## for Loop

Used when the number of repetitions is known.

```python
for i in range(1, 6):
    print(i)
```

---

## range()

```python
range(5)          # 0 1 2 3 4

range(1, 6)       # 1 2 3 4 5

range(2, 11, 2)   # 2 4 6 8 10
```

---

## break

Stops the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
```

---

## continue

Skips the current iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output:

```
0
1
3
4
```

---

## Infinite Loop

```python
while True:
    print("Running")
```

Use `break` to stop it.

---

## Best Practices

- Use `for` when the number of iterations is known.
- Use `while` when repetition depends on a condition.
- Update variables inside a `while` loop.
- Keep loops simple.
- Avoid unnecessary nesting.

---

## Common Mistakes

❌ Forgetting to update the loop variable.

```python
count = 1

while count <= 5:
    print(count)
```

This never ends.

Correct:

```python
count += 1
```

---

## Key Takeaways

- Loops reduce repeated code.
- `for` loops are used for fixed iterations.
- `while` loops depend on a condition.
- `break` exits a loop.
- `continue` skips the current iteration.