# Mini Project: JSON-based log file analyzer
import json

f = open("logs.json", "r")
logs = json.load(f)
f.close()

summary = {}
errors = []
for log in logs:
    level = log["level"]
    if level in summary:
        summary[level] = summary[level] + 1
    else:
        summary[level] = 1
    if level == "ERROR":
        errors.append(log)

print("Total logs:", len(logs))
print("Count by level:", summary)
print("\nError messages:")
for e in errors:
    print(e["time"], "-", e["message"])

result = {"total": len(logs), "by_level": summary, "errors": errors}
f = open("log_summary.json", "w")
json.dump(result, f, indent=4)
f.close()
print("\nSummary saved to log_summary.json")
