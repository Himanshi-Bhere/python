# student grade analyzer ask user for maks range 0 to 100 

student_marks = float(input("Enter you marks (0-100): "))

if student_marks >= 90 and student_marks <= 100:
    print("Grade : A+")
elif student_marks >= 80 and student_marks <= 89:
    print("Grade: A")
elif student_marks >= 70 and student_marks <= 79:
    print("Grade: B")
elif student_marks >= 60 and student_marks <= 69:
    print("Grade: C")
elif student_marks >= 50 and student_marks <= 59:
    print("Grade: D")
elif student_marks < 50 :
    print("Grade: F")
else:
    print("Invalid marks. Please enter a valid marks between 0 to 100.")
    