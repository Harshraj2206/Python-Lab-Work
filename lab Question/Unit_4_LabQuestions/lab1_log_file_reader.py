# Lab Exercise 1: Log file reader program

f = open("app.log", "r")
lines = f.readlines()
f.close()

info = 0
warning = 0
error = 0

print("Error lines:")
for line in lines:
    if "INFO" in line:
        info = info + 1
    elif "WARNING" in line:
        warning = warning + 1
    elif "ERROR" in line:
        error = error + 1
        print(line.strip())

print("\nTotal lines:", len(lines))
print("INFO:", info)
print("WARNING:", warning)
print("ERROR:", error)
