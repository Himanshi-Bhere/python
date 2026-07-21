""" Display:
First 3 logs
Last 3 logs
Middle 4 logs
Every alternate log
Logs in reverse order """

logs = [
    "Log1",
    "Log2",
    "Log3",
    "Log4",
    "Log5",
    "Log6",
    "Log7",
    "Log8"
]

print("First 3 logs: ", logs[:3])
print("Last 3 logs: ", logs[-3:])
print("Middle 4 Logs: ", logs[2:6])
print("Every alternate log: ", logs[::2])
print("Logs in reverse order: ", logs[::-1])
