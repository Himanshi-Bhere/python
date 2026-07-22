"""Display: Employee ID, Employee Name, Role, Salary using a loop.
Then update Rahul's salary to 85000.
Print the updated table."""


employees = [
    ["E101", "Himanshi", "Cloud Engineer", 85000],
    ["E102", "Rahul", "Backend Developer", 78000],
    ["E103", "Sara", "AI Engineer", 92000]
]

for employee in employees:
    print(
        f" Employee ID: {employee[0]} "
        )
    print(
        f" Employee Name: {employee[1]} "
        )
    print(
        f" Role: {employee[2]} "
        )
    print(
        f" Salary: {employee[3]} "
        )
    print("-----------------------------")
    # Update Rahul's salary to 85000
    if employee[1] ==  "Rahul":
        employee[3] = 85000
        print(f"Updated salary for {employee[1]}: {employee[3]}")
        
#Print updated table 
print("Updated Employee Directory:")
for employee in employees:
    print(
        f" Employee ID: {employee[0]} "
        )
    print(
        f" Employee Name: {employee[1]} "
        )
    print(
        f" Role: {employee[2]} "
        )
    print(
        f" Salary: {employee[3]} "
        )
    print("-----------------------------")  

        