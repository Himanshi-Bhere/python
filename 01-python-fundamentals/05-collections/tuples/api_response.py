""" Create this tuple:
response = (200, "Success", 1.25)
Where: Status Code, Message, Response Time Using tuple unpacking:"""

response = (200, "Success", 1.25)

status_code, message, response_time = response

print(f"Status Code: {status_code}")
print(f"Message: {message}")
print(f"Response Time: {response_time}")

# This will raise an error because tuples are immutable

response[0] = 500