file = open("employees.txt", "r") # open file in read mode

print(file.readline())
print(file.readline())

file.close() # close the file after reading
