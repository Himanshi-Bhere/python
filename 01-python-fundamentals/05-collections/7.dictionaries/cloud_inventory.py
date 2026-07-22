server = {
    "hostname":"web-server-01",
    "ip":"192.168.1.10",
    "os":"Ubuntu 24.04",
    "cpu":8,
    "memory":"16GB"
}

print("Server Hostname:", server["hostname"])
print("Server IP:", server["ip"])
print("OS:", server["os"])
print("CPU:", server["cpu"])
print("Memory:", server["memory"])

server["memory"] = "32GB"
server["status"] = "Running"
del server["cpu"]
print("Updated Server Details:", server)
