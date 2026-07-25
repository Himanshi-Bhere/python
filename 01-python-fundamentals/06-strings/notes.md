# Python Strings

## 1. What is a String?

A string is a sequence of Unicode characters used to represent textual data.

```python
name = "Himanshi"
server = "prod-web-mumbai-01"
status = "Running"
```

The Python data type for strings is:

```python
str
```

Example:

```python
server = "web-server"

print(type(server))
```

Output:

```text
<class 'str'>
```

---

# 2. String Indexing

Since strings are ordered sequences, every character has an index.

Example:

```python
server = "prod-web-mumbai-01"
```

Indexes begin from `0`.

```python
print(server[0])
```

Output:

```text
p
```

Negative indexes access characters from the end.

```python
print(server[-1])
```

Output:

```text
1
```

Important:

```text
Positive indexing → starts from left at 0
Negative indexing → starts from right at -1
```

---

# 3. String Slicing

Syntax:

```python
string[start:stop:step]
```

The `stop` position is excluded.

Example:

```python
server = "prod-web-mumbai-01"

print(server[0:4])
```

Output:

```text
prod
```

The starting index can be omitted:

```python
print(server[:4])
```

Output:

```text
prod
```

Access the last two characters:

```python
print(server[-2:])
```

Output:

```text
01
```

---

# 4. String Length

`len()` returns the number of characters in a string.

```python
server = "prod-web-mumbai-01"

print(len(server))
```

Output:

```text
18
```

Spaces and special characters are also counted as characters.

---

# 5. Strings are Immutable

Strings cannot be modified in place after they are created.

This will fail:

```python
server = "web-server"

server[0] = "W"
```

Python raises:

```text
TypeError: 'str' object does not support item assignment
```

However, a variable can be assigned a new string:

```python
server = "web-server"
server = "api-server"
```

The original string was not modified. The variable now references another string.

---

# 6. strip()

`strip()` removes leading and trailing whitespace.

Example:

```python
message = "   Server Running   "

clean_message = message.strip()

print(clean_message)
```

Output:

```text
Server Running
```

It does not normally remove spaces inside the text.

---

# 7. upper()

`upper()` returns an uppercase version of a string.

```python
service = "payment-service"

service = service.upper()

print(service)
```

Output:

```text
PAYMENT-SERVICE
```

---

# 8. lower()

`lower()` returns a lowercase version of a string.

```python
status = "RUNNING"

print(status.lower())
```

Output:

```text
running
```

This is useful when normalizing user input.

Example:

```python
user_input = "ERROR"

if user_input.lower() == "error":
    print("Error detected")
```

---

# 9. replace()

`replace()` replaces text and returns a new string.

```python
message = "Database connection failed"

message = message.replace("Database", "DB")

print(message)
```

Output:

```text
DB connection failed
```

Because strings are immutable, `replace()` does not modify the original string object in place.

---

# 10. split()

`split()` separates a string and returns a list.

Example:

```python
server = "prod-web-mumbai-01"

parts = server.split("-")

print(parts)
```

Output:

```text
['prod', 'web', 'mumbai', '01']
```

The transformation is:

```text
String
   ↓
split()
   ↓
List
```

Now individual components can be accessed using list indexing:

```python
environment = parts[0]
service = parts[1]
region = parts[2]
instance = parts[3]
```

---

# 11. Splitting Logs

Structured logs often contain delimiters.

Example:

```python
log = "2026-07-25|ERROR|payment-service|Database connection failed"
```

Split using `|`:

```python
log_parts = log.split("|")
```

Result:

```python
[
    "2026-07-25",
    "ERROR",
    "payment-service",
    "Database connection failed"
]
```

Extract individual fields:

```python
date = log_parts[0]
log_level = log_parts[1]
service = log_parts[2]
message = log_parts[3]
```

---

# 12. String Membership

The `in` operator checks whether text exists inside another string.

```python
log = "ERROR Database connection failed"

print("ERROR" in log)
```

Output:

```text
True
```

Example:

```python
if "ERROR" in log:
    print("Error detected")
```

`not in` performs the opposite check.

```python
print("WARNING" not in log)
```

---

# 13. Method Chaining

String methods can sometimes be chained.

Example:

```python
message = "   SERVER RUNNING   "

clean_message = message.strip().lower()

print(clean_message)
```

Output:

```text
server running
```

Processing happens sequentially:

```text
"   SERVER RUNNING   "
          ↓ strip()
"SERVER RUNNING"
          ↓ lower()
"server running"
```

---

# 14. Real-World Uses of Strings

Strings are heavily used in:

- Log processing
- API responses
- HTTP data
- User input
- File paths
- File names
- Environment variables
- Cloud resource identifiers
- Configuration files
- URLs
- Command-line output
- Network data
- Automation scripts

Example server identifier:

```text
prod-web-mumbai-01
```

A Python program can parse this into:

```text
Environment → prod
Service     → web
Region      → mumbai
Instance    → 01
```

---

# 15. Important String Operations

```python
text[index]
```

Access a character.

```python
text[start:stop]
```

Slice a string.

```python
len(text)
```

Get string length.

```python
text.strip()
```

Remove surrounding whitespace.

```python
text.upper()
```

Convert to uppercase.

```python
text.lower()
```

Convert to lowercase.

```python
text.replace(old, new)
```

Replace text.

```python
text.split(delimiter)
```

Split a string into a list.

```python
"value" in text
```

Check membership.

---

# Exercises Completed

## server_parser.py

Practiced:

- String indexing
- Negative indexing
- String slicing
- `len()`
- Parsing structured identifiers

## log_parser.py

Practiced:

- Cleaning strings using `strip()`
- Splitting structured data using `split()`
- Extracting fields
- `upper()`
- `replace()`
- Membership checking
- Combining strings and lists
- Basic structured log parsing

---

# Key Takeaways

- Strings represent textual data.
- Strings are ordered sequences.
- Strings support indexing and slicing.
- Strings are immutable.
- String methods return processed values rather than modifying the original string in place.
- `strip()` cleans surrounding whitespace.
- `upper()` and `lower()` normalize text.
- `replace()` performs text replacement.
- `split()` converts structured text into a list.
- `in` and `not in` test membership.
- String processing is fundamental to APIs, logs, automation, networking and cloud engineering.