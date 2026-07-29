# String Formatting

String formatting is used to create clean, readable, and professional output.

It is widely used in:

- Backend Development
- Cloud Automation
- DevOps
- APIs
- Monitoring Systems
- Reports
- Logging

---

# f-Strings

The modern and recommended way to insert variables into strings.

Syntax

```python
name = "Himanshi"

print(f"Hello {name}")
```

Output

```
Hello Himanshi
```

---

# Decimal Formatting

Display only a fixed number of decimal places.

Syntax

```python
value = 37.45678

print(f"{value:.2f}")
```

Output

```
37.46
```

Explanation

```
:

Formatting begins

.2

↓

2 digits after decimal

f

↓

Floating point number
```

---

# Percentage Formatting

Example

```python
cpu = 45.786

print(f"{cpu:.2f}%")
```

Output

```
45.79%
```

---

# Thousands Separator

Large numbers become easier to read.

Without formatting

```
850000
```

With formatting

```python
salary = 850000

print(f"{salary:,}")
```

Output

```
850,000
```

Another example

```
12500000

↓

12,500,000
```

---

# Printing Units

Units can be added directly inside f-strings.

Example

```python
memory = 16

print(f"{memory} GB")
```

Output

```
16 GB
```

---

# Label Alignment

Reports become cleaner when labels have equal width.

Example

```python
print(f"{'Hostname':<12}: web-server-01")
print(f"{'Status':<12}: Running")
```

Output

```
Hostname    : web-server-01
Status      : Running
```

`<12`

means

```
Left align

Reserve 12 spaces
```

Similarly

```python
print(f"{'CPU Usage':<12}: {cpu:.2f}%")
```

---

# Why Use Formatting?

Instead of

```
37.456789
```

Display

```
37.46
```

Instead of

```
850000
```

Display

```
850,000
```

Instead of

```
Memory 16
```

Display

```
Memory : 16 GB
```

Professional software always formats output for readability.

---

# Industry Applications

Cloud Monitoring

```
CPU Usage : 35.78%
Memory    : 16 GB
Disk      : 512 GB
```

Employee Reports

```
Salary : $850,000
Bonus  : $85,000
```

Server Reports

```
Hostname : web-server-01
Status   : Running
```

API Reports

```
Status Code : 200
Latency     : 15.23 ms
```

---

# Best Practices

✔ Prefer f-strings over string concatenation.

✔ Format floating-point values to a reasonable number of decimal places.

✔ Use thousands separators for large numbers.

✔ Include units such as GB, MB, ms, %, etc.

✔ Align labels to produce professional CLI reports.