file = open("sample.txt", "r") # open file in read mode

print("complete the file content:")
print("--------------------------------")
print(file.read(7)) # read first 7 characters of the file
print(file.read()) # read the rest of the file

file.close() #close the file after reading 

file = open("sample.txt", "r") # open file in read mode

print("complete the file content:")
print("--------------------------------")
print(file.read(7)) # read first 7 characters of the file
print(file.read()) # read the rest of the file

file.close() #close the file after reading 
