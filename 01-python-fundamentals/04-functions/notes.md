# Lesson 4 - Functions

## What is a Function?

A function is a reusable block of code that performs a specific task.

Instead of writing the same code multiple times, write it once and call it whenever needed.

---

## Creating a Function

```python
def greet():
    print("Hello")
```

Calling:

```python
greet()
```

---

## Parameters

Parameters allow a function to receive input.

```python
def greet(name):
    print(f"Hello {name}")```

```python
greet("Himanshi")
```

---

## Return

`return` sends a value back to the caller.

```python
def add(a, b):
    return a + b ```

```pythonresult = add(10, 20)
print(result)
```


Use `return` when the result will be used later.

---

## Difference Between print() and return

### print()

Displays output.

```python
def add(a, b):
    print(a + b)
```

---

### return

Returns a value.

```python
def add(a, b):
    return a + b
```

`return` is preferred in reusable functions.

---

## Local Variables

Variables created inside a function.

```python
def demo():
    x = 10
```

Cannot be accessed outside the function.

---

## Global Variables

Variables declared outside functions.

```python
college = "KCCEMSR"
```

Accessible inside functions.

Avoid modifying global variables whenever possible.

---

## Default Parameters

```python
def greet(name="Guest"):
    print(f"Hello {name}")```

---
## Keyword Arguments

```python
student(
    name="Himanshi",
    age=21
)
```

Improves readability.

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

# Best Practices

- One function should perform one task.
- Keep functions small.
- Use meaningful function names.
- Prefer `return` over `print` when possible.
- Avoid global variables.

---

# Common Mistakes

❌ Writing one huge function.

❌ Using `print()` everywhere instead of `return`.

❌ Using unclear function names.

```python
def abc():
```

Better

```python
def calculate_total():
```

---

# Key Takeaways

- Functions make code reusable.
- Parameters pass data into functions.
- `return` sends data back.
- Local variables exist only inside functions.
- Small functions are easier to test and maintain.