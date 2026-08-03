username = "   Himanshi_Bhere   "
email = " HIMANSHI@GMAIL.COM "
role = " CLOUD ENGINEER "
# remove unwanted spaces
username = username.strip()
email = email.strip()
role = role.strip()
# print user profile
print("=================================")
print("USER PROFILE")
print("=================================")
print(f"Username: {username.lower()}")
print(f"Email: {email.lower()}")
print(f"Role: {role.title()}")
# check the email is valid or not
if "@" in email and email.endswith(".com"):
    print("Valid Email: True")
else:
    print("Valid Email: False")
    
