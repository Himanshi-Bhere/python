# Display: First task, Last task, Total number of tasks, Then print all tasks one by one using a loop.

task = [
    "Login",
    "upload file",
    "generate report",
    "send email",
    "logout"
]
print("First task:", task[0])
print("Last task:", task[-1])
print("Total number of task:", len(task))

for i, task in enumerate(task, start=1):
    print(f"{i}: {task}")