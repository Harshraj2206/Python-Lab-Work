# Lab Exercise 1: Log file reader program
import os

file_path = os.path.join(os.path.dirname(__file__), "app.log")

try:
    with open(file_path, "r") as f:
        first = f.readline()
        print("First line:", first.strip())
        lines = [first] + f.readlines()
except FileNotFoundError:
    print("Log file not found.")
else:
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for line in lines:
        for level in counts:
            if level in line:
                counts[level] += 1

    print("\nError lines:")
    for line in lines:
        if "ERROR" in line:
            print(line.strip())

    print("\nSummary:", counts)
finally:
    print("Log reading finished.")
