""" use list 
generate report using  loop """

inventory = []
for item in inventory:
    inventory.append(f"Product: {item['Product']}\n")
    inventory.append(f"Status: {item['Status']}\n\n")
    
with open("inventory.txt", "w") as file:
    file.writelines(inventory)
   
        