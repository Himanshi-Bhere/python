""" Program should
open file
calculate total students
average marks
highest mark
topper name
handle file-not-found error
handle any unexpected exception
always print
Analysis Complete
Hint : split(",")
int()
keep track of highest mark
use variables like highest_marks and topper """

filename = "marks.txt"

print("=" *40)
print("STUDENT MARKS ANALYZER")
print("=" *40)

students = [
    "Rahul, 85\n",
    "Sara, 92\n",
    "Amit, 70\n",
    "Priya, 105\n",
    "Himanshu, 95\n",
    "Rohit, 88\n",
]

try: 
    file = open(filename, "r")
    file.readlines(students)
    
    print(f"Total Students : {len(students)}")
    
    for student in students:
        if student:
            name, marks = student.split(",")
            print(f"{name.strip()} : {marks.strip()}")
        
    
    # average marks highest mark topper name    
    total_marks = 0
    highest_marks = 0
    topper = ""
    
    for student in students:
        if student:
            name, marks = student.split(",")
            marks = int(marks.strip())
            total_marks += marks
            if marks > highest_marks:
                highest_marks = marks
                topper = name.strip()
    file.close()
    print(f"Average Marks : {total_marks / len(students):.2f}")
    print(f"Highest Marks : {highest_marks}")
    print(f"Topper : {topper}")
    print("Analysis Complete") # print Analysis Complete if sucessfull

except FileNotFoundError:
    print('ERROR')
    print(f"file {filename} not found")
    print("please verify that the file exists")

except Exception as error:
    print('ERROR')
    print(f"An unexpected error occurred: {error}")

finally:
    print("=" *40)
    print("Closing Student Marks Analyzer...")
    print("=" *40)
    