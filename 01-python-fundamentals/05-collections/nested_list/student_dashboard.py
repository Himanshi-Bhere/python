""" Display:
Each student's marks.
Average marks of each student.
Highest Python score.
Student who scored the highest in Python.
Hint: You already know loops, lists, indexing, len(), and arithmetic. """

students = [
    ["Himanshi", 85, 92, 75],
    ["Rahul", 78, 88, 90],
    ["Sara", 92, 66, 80],
    ["Amit", 70, 95, 88]
]

# Display each student's marks
for student in students:
    print(f"Student NAME: {student[0]}")
    print(f"Python Marks: {student[1]}")
    print(f"Math Marks: {student[2]}")
    print(f"Science Marks: {student[3]}")
    print("-----------------------------")

# Calculate average marks of each student
for student in students:
    average_marks = (student[1] + student[2] + student[3]) / 3
    print(f"Average marks of {student[0]}: {average_marks:.2f}") # 2f is used to format the average marks to 2 decimal places
    print("-----------------------------")
    
# Find the highest Python score  
highest_python_score = max(student[1] for student in students)
print(f"Highest Python score: {highest_python_score}")
   
# Find the student who scored the highest in Python
for student in students:
    if student[1] == highest_python_score:
        print(f"Student who scored the highest in python: {student[0]}")
            