# Create an empty list called workflow.
# Ask the user to enter 5 workflow steps.
# Add each step to the list. 

workflow = [] 

for i in range (5):
    step = input(f"Please enter workflow steps {i+1}: ")
    workflow.append(step)
    
print("\n Workflow Created")
for i, step in enumerate(workflow, start=1): # enumerate is used to get the index and value of each step in the workflow list, starting the index from 1
    print(f"{i}: {step}")

    