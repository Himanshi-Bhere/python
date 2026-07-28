

address = input("Enter server address: ")

address = address.strip() # Remove surrounding whitespaces

parts = address.split("-")
print(f"Server address parts: {parts}")

if len(parts) == 2:
    server = parts[0]
    port = parts[1]

    if server.isalpha() and port.isdigit():
        print("Valid server")
    else:
        print("Invalid server")
else:
    print("Invalid format")