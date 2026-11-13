# Mini Project: Attendance Tracker
from datetime import date

students = input("Enter student names (comma separated): ").split(",")
students = [s.strip() for s in students]

attendance = {s: [] for s in students}

days = int(input("Enter number of days: "))
for d in range(days):
    print(f"\nDay {d + 1}")
    for s in students:
        status = input(f"Is {s} present? (y/n): ").lower()
        attendance[s].append(status == "y")

print("\nAttendance Report -", date.today())
print("Name\tPresent\tPercentage")
for s, record in attendance.items():
    present = sum(record)
    percent = present / days * 100
    print(f"{s}\t{present}/{days}\t{percent:.1f}%")

low = [s for s, r in attendance.items() if sum(r) / days * 100 < 75]
print("\nStudents below 75%:", low if low else "None")
