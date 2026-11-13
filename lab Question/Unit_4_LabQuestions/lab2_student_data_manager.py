# Lab Exercise 2: Student data manager using files
import os

file_path = os.path.join(os.path.dirname(__file__), "students.txt")

while True:
    print("\n1. Add student  2. View students  3. Search student  4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Roll number: ")
        name = input("Name: ")
        marks = input("Marks: ")
        with open(file_path, "a") as f:
            f.write(f"{roll},{name},{marks}\n")
        print("Student saved.")

    elif choice == "2":
        try:
            with open(file_path, "r") as f:
                for line in f:
                    roll, name, marks = line.strip().split(",")
                    print(roll, name, marks)
        except FileNotFoundError:
            print("No records found.")

    elif choice == "3":
        roll_no = input("Enter roll number: ")
        try:
            with open(file_path, "r") as f:
                for line in f:
                    roll, name, marks = line.strip().split(",")
                    if roll == roll_no:
                        print(roll, name, marks)
                        break
                else:
                    print("Student not found.")
        except FileNotFoundError:
            print("No records found.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
