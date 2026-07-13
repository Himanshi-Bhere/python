# password strength has_uppercase ,has_lowercase, has_number, has_special_character, has_length

def password_strength(password):
    #check the length 
    if len(password) < 8:
        return "Weak password: Password must be at least 8 characters long."
    
    #check for uppercase letter
    if not any(char.isupper() for char in password):
        return "Weak password: Password must contain at least one uppercase letter."
    
    #check for lowercase letter
    if not any(char.islower() for char in password):
        return "Weak password: Password must contain at least one lowercase letter."
    
    # check for number
    if not any(char.isdigit() for char in password):
        return "Weak password: Password must contain at least one number."
    
    # check for special character
    special_characters = "!@#$%^&*()-+"
    if not any(char in special_characters for char in password):
        return "Weak password: Password must contain at least one special character."
    
    return "Strong password!"
password = input("Please enter a password: ")
strength = password_strength(password)
print(strength)
