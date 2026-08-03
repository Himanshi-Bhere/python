log = "2026-07-29|ERROR|PAYMENT-SERVICE|Database connection failed"
print("Original Log Entry:",log)
parts = log.split("|") # Split the log entries
date = parts[0] # Extract the data
level = parts[1]
service = parts[2]
message = parts[3]
print("=================================") #print the clean log analysis report
print("CLEAN LOG ANALYSIS REPORT")
print("=================================")
print("Date:",date)
print("Level:",level)
print("Service:",service)
print("Service (lower):",service.lower())
print("Message:",message)
print("Message Length:",len(message)) # length of the message
if "ERROR" in level: # check if ERROR exists
    print("Contains ERROR:",True)
print("=================================")
    


    

    