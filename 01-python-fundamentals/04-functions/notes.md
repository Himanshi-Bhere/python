# Lesson 4 - Functions

## What is a Function?

A function is a reusable block of code that performs a specific task.

Instead of writing the same code multiple times, write it once and call it whenever needed.

---

## Defining a Function

```python
def greet():
    print("Hello")
```

Call it:

```python
greet()
```

---

## Parameters

Parameters allow functions to receive input.

```python
def greet(name):
    print(f"Hello {name}")
```

Example:

```python
greet("Himanshi")
```

---

## Return

`return` sends a value back to the caller.

```python
def add(a, b):
    return a + b
```

Example:

```python
result = add(10, 20)

print(result)
```

---

## print() vs return

Using `print()`:

```python
def add(a, b):
    print(a + b)
```

Displays the result but cannot be reused.

Using `return`:

```python
def add(a, b):
    return a + b
```

Returns the value so it can be stored, used in calculations, or passed to other functions.

---

## Local Variables

Variables created inside a function exist only inside that function.

```python
def demo():
    x = 10
```

Outside the function, `x` does not exist.

---

## Global Variables

Variables created outside functions.

```python
college = "KCCEMSR"
```

Can be accessed inside functions.

Avoid modifying global variables unless necessary.

---

## Default Parameters

```python
def greet(name="Guest"):
    print(f"Hello {name}")
```

If no value is passed:

```
Hello Guest
```

---

## Keyword Arguments

Instead of:

```python
student("Himanshi", 21, "EXTC")
```

You can write:

```python
student(
    name="Himanshi",
    age=21,
    branch="EXTC"
)
```

This improves readability.

---

## *args

Accepts multiple positional arguments.

```python
def total(*numbers):
    return sum(numbers)
```

---

## **kwargs

Accepts multiple keyword arguments.

```python
def profile(**details):
    print(details)
```

---

## Best Practices

- One function should do one job.
- Keep functions short.
- Use meaningful names.
- Return values instead of printing whenever possible.
- Avoid duplicate code.

---

## Common Mistakes

❌ Forgetting to call the function.

```python
def greet():
    print("Hello")
```

Nothing happens until:

```python
greet()
```

---

❌ Printing instead of returning when the value needs to be reused.

---

## Key Takeaways

- Functions make code reusable.
- Parameters pass data into functions.
- `return` sends data back.
- Local variables exist only inside functions.
- Keep functions small and focused.