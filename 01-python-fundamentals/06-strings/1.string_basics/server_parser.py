# string [using slices]

server = "prod-web-mumbai-01"

print(f"Server identifier: {server}")
print(f"First character: {server[0]}")
print(f"Last character: {server[-1]}")
print(f"Environment: {server[0:4]}")
print(f"Service: {server[5:8]}")
print(f"Instance number: {server[-2:]}")
print(f"Identifier length: {len(server)}")