file = open("employees.txt","r")
lines = file.readlines()
print(lines)
print("Total number of lines:", len(lines))
for line in lines: # print new line after each line
    print(line)
# remove \n from each line 
for line in lines:
    print(line.strip())
print("Lines after removing \\n:")
print(lines)
file.close()