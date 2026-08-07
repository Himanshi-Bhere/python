students = [
    "Rahul\n",
    "Sara\n",
    "Amit\n",
    "Priya\n",
    "Himanshu\n"
]
file = open("students.txt", "w")
file.writelines(students)
file.close()
