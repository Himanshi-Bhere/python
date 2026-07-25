# dictionaries methods

config = {
    "provider":"AWS",
    "region":"ap-south-1",
    "instance":"t3.micro",
    "storage":"100GB"
}

# print every key-value pair using items()
print(config.items())

# print avaliable settings using keys()
print(config.keys())

# print all values using values()
print(config.values())

# safely read backup region using get()
print(config.get("backup_region", "Not configured"))

# update the dictionary using update()
config.update({
    "storage": "250GB",
    "status": "Running"
})
print("updated config:", config)


# remove instance using pop()
config.pop("instance")

# creat backup_cinfig using copy()
backup_config = config.copy()
print("backup config:", backup_config)
