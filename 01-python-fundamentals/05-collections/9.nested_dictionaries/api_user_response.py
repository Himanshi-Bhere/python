# nested dictionaries 

response = {
    "status": 200,
    "message": "Users retrieved successfully",

    "data": {
        "U101": {
            "username": "himanshi",
            "role": "cloud_engineer",
            "active": True
        },

        "U102": {
            "username": "rahul",
            "role": "backend_developer",
            "active": False
        },

        "U103": {
            "username": "sara",
            "role": "devops_engineer",
            "active": True
        }
    }
}

# print status and message from the response
print(f"Status: {response['status']}")
print(f"Message: {response['message']}")

# access and print the username of user U102
print(f"Username of U102: {response['data']['U102']['username']}")
print(f"Role of U103: {response['data']['U103']['role']}")

# change the active status of user U102 to True
response['data']['U102']['active'] = True
print(f"Active status of U102: {response['data']['U102']['active']}")
print("--------------------")


#loop through all users and print their details
for user_id, user_details in response['data'].items():
    print(f"User ID: {user_id}")
    for key, value in user_details.items():
        print(f"{key}: {value}")
    print("--------------------")
    
    
# totla user and active user 
active_count = 0

for user_id, user_details in response["data"].items():
    if user_details["active"]:
        active_count += 1

total_users = len(response["data"])

print(f"Total Users: {total_users}")
print(f"Active Users: {active_count}")