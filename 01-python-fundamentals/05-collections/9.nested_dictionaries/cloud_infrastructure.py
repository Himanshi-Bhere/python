# nested dictionaries

from http import server


infrastructure = {
    "web-server-01":{
    "IP": "10.0.1.10",
    "CPU": 4,
    "Memory": "8GB",
    "Status": "Running"
    },
    "api-server-01": {
    "IP": "10.0.1.20",
    "CPU": 8,
    "Memory": "16GB",
    "Status": "Running"
    },
    "worker-server-01": {
    "IP": "10.0.1.30",
    "CPU": 8,
    "Memory": "32GB",
    "Status": "Stopped"
    }
}

# print ip address of api-server-01
print(infrastructure["api-server-01"]["IP"])

# print memory of worker-server-01
print(infrastructure["worker-server-01"]["Memory"])

# change status of worker-server-01 to Running and memory to 16GB
infrastructure["worker-server-01"]["Status"] = "Running"
print(infrastructure["worker-server-01"]["Status"])
infrastructure["worker-server-01"]["Memory"] = "16GB"
print(infrastructure["worker-server-01"]["Memory"])
print("--------------------")


# then loop through all servers and produce 

for server, details in infrastructure.items():
    print(f"Server: {server}")
    for key, value in details.items():
        print(f"{key}: {value}") 
    print("--------------------")

        