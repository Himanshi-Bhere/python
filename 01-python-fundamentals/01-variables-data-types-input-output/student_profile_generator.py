# Print a neatly formatted profile of a student using the given details.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
college = input("Enter your college name: ")
branch = input("Enter your branch: ")
year = (input("Enter your year of study: "))
skills = input("Enter your skills: ")
dream_job = input("Enter your dream job: ")

print("\n ======Student Profile======")
print(f"Name : {name}")
print(f"Age : {age}")
print(f"College : {college}")
print(f"Branch : {branch}")
print(f"Year of Study : {year}")
print(f"Skills : {skills}")
print(f"Dream Job : {dream_job}")
print("===============================")