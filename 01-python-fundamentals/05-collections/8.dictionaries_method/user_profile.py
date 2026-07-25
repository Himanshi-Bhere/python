# dictionaries methods

user = {
    "username": "himanshi",
    "email": "himanshi@gmail.com",
    "role": "Cloud Engineer",
    "experience": 2
}

# print user content using get()
print(user.get("username"))
print(user.get("email"))
print(user.get("role"))
print(user.get("experience",0))

# print all keys using key()
print(user.keys())

# print all values using values()
print(user.values())

# print every key-value pair using items()
print(user.items())

# update the dictionary using update()
user.update(
    {"city": "Mumbai",
     "salary": 90000}
)
print("updated user:", user)

# remove experience key-value pair using pop()
user.pop("experience")

# create a copy backup_user using copy()
backup_user = user.copy()
print("backup user:", backup_user)