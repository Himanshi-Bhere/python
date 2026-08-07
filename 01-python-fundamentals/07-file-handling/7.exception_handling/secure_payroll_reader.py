filename = "payroll.txt"

print("=" *40)
print("EMPLOYEE PAYROLL SYSTEM")
print("=" *40)

salary = [
    "Rahul : 850000\n",
    "Sara : 92000\n",
    "Amit : 70000\n",
    "Priya : 105000\n"
]

try: 
    file = open(filename, "w")
    file.writelines(salary)
    
    print(f"Total EMPLOYES: {len(salary)}")
    print()
    
    for employee in salary:
        if employee:
            print(f"{employee.split(':')[0]} {employee.split(':')[1].strip()}")
    file.close()
    print("payload loaded successfully") # print pyload loaded successfully if sucessfull
    
except FileNotFoundError:
    print('ERROR')
    print(f"file {filename} not found")
    print("please verify that the file exists")

except PermissionError:
    print('ERROR')
    print(f"Permission denied while opening the file {filename}")
    
except Exception as error:
    print('ERROR')
    print(f"An unexpected error occurred: {error}")
    
finally:
    print("=" *40)
    print("Closing payroll system...")
    print("=" *40)
    