""" Display:
Number of "Testing" tasks.
Index of "Deployment".
Create a copy of the list.
Sort the copied list.
Reverse the copied list.
Print both the original and copied list to show the original remains unchanged. """

tasks = [
    "Meeting",
    "Code Review",
    "Testing",
    "Deployment",
    "Testing"
]

print("Number of testing tasks: ", tasks.count("Testing"))
print("Index of Deployment: ", tasks.index("Deployment"))

# Create a copy of list
copied_tasks = tasks.copy()

# Sort the copied list 
copied_tasks.sort()
print("Sorted copied list: ", copied_tasks)

# Reverse the copied list 
copied_tasks.reverse()
print("Reversed copied list: ", copied_tasks)

# Print both the original and copied list to show the original remains unchanged.
print("\n Original list: ", tasks)
print("Copied list: ", copied_tasks)