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
    return "F"


students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"Student {i + 1} name: ")
    marks = list(map(int, input("Enter marks of 3 subjects (space separated): ").split()))
    students[name] = marks

print("\nName\tTotal\tAverage\tGrade")
for name, marks in students.items():
    total = sum(marks)
    avg = total / len(marks)
    print(f"{name}\t{total}\t{avg:.2f}\t{get_grade(avg)}")
