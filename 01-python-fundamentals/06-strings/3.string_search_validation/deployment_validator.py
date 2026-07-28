"""Without me giving you the solution, make the program:
Remove accidental surrounding spaces.
Check whether the artifact ends with .zip.
Check whether it starts with payment-service.
Count how many - characters exist.
Find the position where "prod" starts.
Print whether "prod" exists.
Print: """

artifact = input("Enter deployment artifact: ")
artifact = artifact.strip() # Remove accidental surrounding spaces

if artifact.endswith(".zip"): # Check whether the artifact ends with .zip
    print("The artifact ends with .zip")
    
if artifact.startswith("payment-service") : # Check whether it starts with payment-service
    print("The artifact starts with payment-service")
    
print(f"The artifact contains {artifact.count('-')} '-' characters") # Count how many - characters exist
prod_position = artifact.find("prod") # Find the position where "prod" starts

if prod_position != -1: # Check if "prod" exists
    print(f"'prod' starts at position {prod_position}")
else:
    print("'prod' does not exist in the artifact name")
    
print("======")

# print whether the artifact is valid based on the checks
if artifact.endswith(".zip"):
    print("Zip file: True")
else:
    print("Zip file: False")
if artifact.startswith("payment-service"):
    print("Starts with payment-service: True")
else:
    print("Starts with payment-service: False")
if artifact.count('-') > 0:
    print(f"Contains '-' characters: True ({artifact.count('-')} occurrences)")
else:
    print("Contains '-' characters: False")
if prod_position != -1:
    print(f"'prod' exists: True (starts at position {prod_position})")
else:
    print("'prod' exists: False")
if artifact.endswith(".zip") and artifact.startswith("payment-service") and prod_position != -1:
    print("The artifact is valid for deployment.")