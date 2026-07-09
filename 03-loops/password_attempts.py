# loops with the condition logic to limit the number of password attempts

correct_password = "Himanshi123"
max_attempts = 3 
attempts = 0
 
while attempts < max_attempts:
    password = input("Enter your pasword:")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        attempts += 1 
        print(f"Incorrect password. You have {max_attempts - attempts} attempts left.")
    