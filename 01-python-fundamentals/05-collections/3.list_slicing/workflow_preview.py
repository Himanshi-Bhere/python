"""Print: First 2 steps
Last 2 steps
Every second step
Reverse workflow
Copy the workflow using slicing ([:])"""

workflow = [
    "Read CSV",
    "Validate",
    "Clean",
    "Transform",
    "Generate PDF",
    "Email",
    "Archive"
]
 
print("First 2 steps: ", workflow[:2])
print("Last 2 steps: ", workflow[-2:])
print("Every second step: ", workflow[::2])
print("Reverse workflow: ", workflow[::-1]) 

workflow.append("Send email")
workflow.insert(1, "Clean Data")
copied_workflow = workflow[:]
copied_workflow.sort()

print("original workflow: ", workflow)
print("copied workflow: ", copied_workflow)
