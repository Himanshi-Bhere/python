file = open("server_status.txt","w") #create a new write file 
report = (
    "Hostname: Web-01\n"
    "Status: Running\n"
    "CPU Usage: 49%\n"
    "Memory: 16GB"
)

file.write(report)
file.close() #close the file after writing