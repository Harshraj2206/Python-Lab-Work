# Mini Project: JSON-based log file analyzer
import json
import os

folder = os.path.dirname(__file__)
input_file = os.path.join(folder, "logs.json")
output_file = os.path.join(folder, "log_summary.json")

try:
    with open(input_file, "r") as f:
        logs = json.load(f)
except FileNotFoundError:
    print("logs.json not found.")
    logs = []
except json.JSONDecodeError:
    print("Invalid JSON format.")
    logs = []

summary = {}
for log in logs:
    level = log["level"]
    summary[level] = summary.get(level, 0) + 1

errors = [log for log in logs if log["level"] == "ERROR"]

print("Total logs:", len(logs))
print("Count by level:", summary)
print("\nError messages:")
for e in errors:
    print(e["time"], "-", e["message"])

with open(output_file, "w") as f:
    json.dump({"total": len(logs), "by_level": summary, "errors": errors}, f, indent=4)

print("\nSummary saved to log_summary.json")
