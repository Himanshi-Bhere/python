# Smart_Calculator ask user for first number, operator, and second number  

num1 = float(input("Enter first number: " ))

operator = input("Enter operator (+, -, *, /):")

num2 = float(input("Enter second number:"))

if operator == "+" :
    print(f"Result: {num1 + num2}")
elif operator == "-" :
    print(f"Result: {num1 - num2}")
elif operator == "*" :
    print(f"Result: {num1 * num2}")
elif operator == "/":
    print(f"Result: {num1 / num2}")
else :
    print("IInvalid operator. Please enter a valid operator.")
    