# ask user for numberand print multiplication table of that number using a loop

number = int(input("Enter a number: "))

print(f"Multiplication table of {number}:")
for i in range(1, 11):                      # Loop through numbers 1 to 10
    result = number * i                     
    print(f"{number} x {i} = {result}")
    
    