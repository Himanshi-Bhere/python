employees = { 
            "id": "E101",
            "name" : "John",
            "role": "Software Engineer",
            "salary": 75000,
            "city" : "New York" 
            }
print("Employee Details:")
print("employee id:", employees["id"])
print("employee name:", employees["name"])
print("employee role:", employees["role"])
print("employee salary:", employees["salary"])
print("employee city:", employees["city"])

#update the employee salary
employees["salary"] = 80000
print("Updated employee salary:", employees["salary"])

# add department 
employees["department"] = "cloud"
print("add department:", employees["department"])

# delete city
del employees["city"]


print("updated details of employee:", employees)