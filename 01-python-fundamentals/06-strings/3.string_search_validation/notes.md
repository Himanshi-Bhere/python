# String Search & Validation

String searching and validation methods are widely used in backend systems, cloud automation, networking, log analysis, APIs, and DevOps.

---

## 1. find()

Searches for the first occurrence of a substring.

Syntax:

```python
string.find(substring)
```

Returns:

- Index of the substring if found.
- -1 if not found.

Example:

```python
text = "ERROR database failed"

print(text.find("database"))
```

Output:

```
6
```

If the substring doesn't exist:

```python
print(text.find("warning"))
```

Output:

```
-1
```

---

## 2. count()

Counts how many times a substring appears.

Syntax:

```python
string.count(substring)
```

Example:

```python
text = "ERROR INFO ERROR"

print(text.count("ERROR"))
```

Output:

```
2
```

---

## 3. startswith()

Checks whether a string begins with a specific value.

Syntax:

```python
string.startswith(prefix)
```

Returns:

```
True
False
```

Example:

```python
server = "prod-web-01"

print(server.startswith("prod"))
```

Output:

```
True
```

---

## 4. endswith()

Checks whether a string ends with a specific value.

Syntax:

```python
string.endswith(suffix)
```

Example:

```python
filename = "server.log"

print(filename.endswith(".log"))
```

Output:

```
True
```

---

## 5. isdigit()

Returns True if every character is a digit.

Example:

```python
port = "8080"

print(port.isdigit())
```

Output:

```
True
```

Useful before converting to integer.

---

## 6. isalpha()

Returns True if every character is a letter.

Example:

```python
city = "Mumbai"

print(city.isalpha())
```

Output:

```
True
```

---

## 7. isalnum()

Checks whether a string contains only letters and numbers.

Example:

```python
username = "himanshi123"

print(username.isalnum())
```

Output:

```
True
```

---

## 8. isspace()

Returns True if a string contains only whitespace.

Example:

```python
text = "     "

print(text.isspace())
```

Output:

```
True
```

---

## 9. join()

Joins a list of strings into one string.

Syntax:

```python
separator.join(list)
```

Example:

```python
parts = ["prod", "web", "01"]

server = "-".join(parts)
```

Output:

```
prod-web-01
```

---

## split() vs join()

split()

String
↓

List

join()

List
↓

String

---

## Industry Use Cases

find()

- Search keywords in logs.
- Search services in filenames.
- Detect environments.

count()

- Count ERROR logs.
- Count failed requests.
- Count delimiters.

startswith()

- Validate server names.
- Validate deployment prefixes.
- Check URL prefixes.

endswith()

- Validate file extensions.
- Validate backups.
- Validate configuration files.

isdigit()

- Validate ports.
- Validate IDs.
- Validate numeric user input.

isalpha()

- Validate usernames.
- Validate city names.
- Validate service names.

join()

- Build URLs.
- Build file paths.
- Build server identifiers.

---

## Best Practices

✔ Always validate user input before processing.

✔ Use descriptive Boolean variables.

Example:

```python
is_zip = artifact.endswith(".zip")
has_prod = artifact.find("prod") != -1
```

instead of repeatedly calling the same methods.

✔ Check list length after split() before accessing indexes.

Bad:

```python
parts = address.split("-")

server = parts[0]
port = parts[1]
```

Good:

```python
parts = address.split("-")

if len(parts) == 2:
    server = parts[0]
    port = parts[1]
else:
    print("Invalid format")
```

This prevents IndexError and makes the program more robust.