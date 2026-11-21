# Mini Project: Attendance Tracker

n = int(input("Enter number of students: "))
students = []
for i in range(n):
    students.append(input("Enter student name: "))

present = {}
for s in students:
    present[s] = 0

days = int(input("Enter number of days: "))
for d in range(days):
    print("\nDay", d + 1)
    for s in students:
        status = input("Is " + s + " present? (y/n): ")
        if status == "y":
            present[s] = present[s] + 1

print("\nAttendance Report")
print("Name  Present  Percentage")
for s in students:
    percent = present[s] / days * 100
    print(s, present[s], "/", days, round(percent, 1), "%")

print("\nStudents below 75%:")
for s in students:
    if present[s] / days * 100 < 75:
        print(s)
