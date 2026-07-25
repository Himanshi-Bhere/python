# string  methods 

log = "  2026-07-25|ERROR|payment-service|Database connection failed  "

# remove leading and trailing whitespace
log = log.strip()
print(f"log entry: {log}")

# spilt the clean string using |
log_parts = log.split("|")
print("-------Log Parts-------")
print(f"log_parts: {log_parts}")

# extract the date, log level, service name, and message from the log_parts list
date = log_parts[0]
log_level = log_parts[1]
service_name = log_parts[2]
message = log_parts[3]
print("-------Clean Log Details-------")
print(f"Date: {date}")
print(f"Log Level: {log_level}")
print(f"Service Name: {service_name}")
print(f"Message: {message}")

# covnvert service into uppercase
service_name = service_name.upper()

# replace database with DB
message = message.replace("Database", "DB")

# determaine error exisit in the clean log 
if "ERROR" in log:
    print("Error found in log entry")
    
# print log details 
print("-------Log Details-------")
print(f"Date: {date}")
print(f"Log Level: {log_level}")
print(f"Service Name: {service_name}")
print(f"Message: {message}")
