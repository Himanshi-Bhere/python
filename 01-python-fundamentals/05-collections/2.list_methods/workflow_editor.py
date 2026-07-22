# append , insert , remove , pop , clear , index , count , sort , reverse , copy 

workflow = [
    "Read CSV file",
    "Generate report",
    "Archive report",
    "save the report",
    
]
workflow.append("Send email")
workflow.insert(1, "Clean Data")
workflow.remove("Generate report")
print(workflow.index("Archive report"))
print(workflow.count("save the report"))
print(workflow.pop(-2))

print("\n Workflow Created ")
for i, step in enumerate(workflow, start=1):
    print(f"{i}: {step}")
    