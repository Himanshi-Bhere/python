# Nested Dictionaries in Python

## 1. What is a Nested Dictionary?

A nested dictionary is a dictionary that contains one or more dictionaries as values.

It is useful for representing structured or hierarchical data.

Example:

```python
employee = {
    "name": "Himanshi",
    "role": "Cloud Engineer",
    "contact": {
        "email": "himanshi@example.com",
        "city": "Mumbai"
    }
}

Here, contact is a dictionary stored inside the employee dictionary.

2. Accessing Values in a Nested Dictionary

Values are accessed by moving through the dictionary level by level.

Example:

server = {
    "name": "web-server-01",
    "network": {
        "ip": "192.168.1.10",
        "port": 443
    }
}

Access the server name:

print(server["name"])

Access the entire network dictionary:

print(server["network"])

Access only the IP address:

print(server["network"]["ip"])

The expression:

server["network"]["ip"]

works as:

Access network from server.
network returns another dictionary.
Access ip from that dictionary.
3. Modifying Nested Dictionary Values

Nested dictionary values can be modified using their keys.

Example:

server = {
    "resources": {
        "cpu": 4,
        "memory": "8GB"
    }
}

Update memory:

server["resources"]["memory"] = "16GB"

Result:

{
    "resources": {
        "cpu": 4,
        "memory": "16GB"
    }
}
4. Adding Values to a Nested Dictionary

New key-value pairs can be added to an inner dictionary.

Example:

server["resources"]["storage"] = "100GB"

Now:

{
    "resources": {
        "cpu": 4,
        "memory": "16GB",
        "storage": "100GB"
    }
}
5. Dictionaries Containing Multiple Records

Nested dictionaries are useful when storing multiple related records.

Example:

employees = {
    "E101": {
        "name": "Himanshi",
        "role": "Cloud Engineer"
    },

    "E102": {
        "name": "Rahul",
        "role": "Backend Developer"
    },

    "E103": {
        "name": "Sara",
        "role": "DevOps Engineer"
    }
}

Access an entire employee:

print(employees["E102"])

Access only the employee's role:

print(employees["E102"]["role"])

Output:

Backend Developer
6. Looping Through Nested Dictionaries

The .items() method is useful when both the key and value are required.

Example:

for employee_id, details in employees.items():
    print(employee_id)
    print(details)

Here:

employee_id contains the outer dictionary key.
details contains the inner dictionary.

A more useful example:

for employee_id, details in employees.items():
    print(f"ID: {employee_id}")
    print(f"Name: {details['name']}")
    print(f"Role: {details['role']}")
7. Nested Looping

If we do not know all the keys inside the inner dictionary, another loop can be used.

Example:

for employee_id, details in employees.items():

    print(f"Employee ID: {employee_id}")

    for key, value in details.items():
        print(f"{key}: {value}")

This allows the program to dynamically process all fields.

8. Using .values() with Nested Dictionaries

.values() returns the values stored inside a dictionary.

Example:

users = {
    "U101": {
        "username": "himanshi",
        "active": True
    },

    "U102": {
        "username": "rahul",
        "active": False
    }
}

Using:

users.values()

returns the user dictionaries.

Therefore:

for user in users.values():
    print(user)

loops through every user's information without needing the user IDs.

9. Filtering Nested Dictionary Data

Nested dictionary data can be combined with conditions.

Example:

active_users = []

for user in users.values():
    if user["active"]:
        active_users.append(user)

The same operation can be written using a list comprehension:

active_users = [
    user
    for user in users.values()
    if user["active"]
]

Count active users:

active_count = len(active_users)
10. Counting Records

If every outer dictionary entry represents one record:

total_users = len(users)

For an API-like structure:

response = {
    "status": 200,
    "data": {
        "U101": {...},
        "U102": {...},
        "U103": {...}
    }
}

The number of users is:

total_users = len(response["data"])
11. Nested Dictionaries and APIs

API responses commonly contain nested structures.

Example:

response = {
    "status": 200,
    "message": "Users retrieved successfully",
    "data": {
        "U101": {
            "username": "himanshi",
            "role": "cloud_engineer",
            "active": True
        }
    }
}

Access the status:

response["status"]

Access the data:

response["data"]

Access user U101:

response["data"]["U101"]

Access U101's username:

response["data"]["U101"]["username"]

This pattern is important because JSON responses from REST APIs are commonly converted into Python dictionaries.

12. Nested Dictionaries in Cloud Automation

Cloud infrastructure contains hierarchical data, so nested dictionaries are useful for representing resources.

Example:

infrastructure = {
    "web-server-01": {
        "ip": "10.0.1.10",
        "cpu": 4,
        "memory": "8GB",
        "status": "Running"
    },

    "api-server-01": {
        "ip": "10.0.1.20",
        "cpu": 8,
        "memory": "16GB",
        "status": "Running"
    }
}

This type of structure can represent:

Servers
Virtual machines
Containers
Network configurations
Cloud resources
Application configurations
API responses
User records
Monitoring information
13. Important Patterns

Access nested value:

dictionary["outer_key"]["inner_key"]

Modify nested value:

dictionary["outer_key"]["inner_key"] = new_value

Loop through records:

for key, details in dictionary.items():
    print(key)
    print(details)

Loop through inner values:

for key, details in dictionary.items():
    for inner_key, value in details.items():
        print(inner_key, value)

Get only record values:

for details in dictionary.values():
    print(details)

Count records:

len(dictionary)
14. Key Takeaways
A nested dictionary is a dictionary inside another dictionary.
Nested dictionaries represent hierarchical and structured data.
Nested values are accessed using multiple keys.
Inner values can be added, updated, and deleted.
.items() provides both keys and values while looping.
.values() is useful when only record data is required.
Nested dictionaries can be combined with loops and conditions.
Nested dictionaries are extremely common when working with JSON and APIs.
They are also useful for cloud configuration, infrastructure information, application state, and structured records.