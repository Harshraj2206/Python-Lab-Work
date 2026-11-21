# Lab Exercise 2: Student grading system

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    m1 = int(input("Marks in subject 1: "))
    m2 = int(input("Marks in subject 2: "))
    m3 = int(input("Marks in subject 3: "))
    students[name] = [m1, m2, m3]

print("\nName  Total  Average  Grade")
for name in students:
    marks = students[name]
    total = marks[0] + marks[1] + marks[2]
    avg = total / 3
    print(name, total, round(avg, 2), get_grade(avg))
