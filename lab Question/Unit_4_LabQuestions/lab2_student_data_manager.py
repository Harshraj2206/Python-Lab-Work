# Lab Exercise 2: Student data manager using files

# create the file if it does not exist
open("students.txt", "a").close()

while True:
    print("\n1. Add student  2. View students  3. Search student  4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Roll number: ")
        name = input("Name: ")
        marks = input("Marks: ")
        f = open("students.txt", "a")
        f.write(roll + "," + name + "," + marks + "\n")
        f.close()
        print("Student saved.")

    elif choice == "2":
        f = open("students.txt", "r")
        for line in f:
            print(line.strip())
        f.close()

    elif choice == "3":
        roll_no = input("Enter roll number: ")
        found = False
        f = open("students.txt", "r")
        for line in f:
            data = line.strip().split(",")
            if data[0] == roll_no:
                print(line.strip())
                found = True
        f.close()
        if found == False:
            print("Student not found.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
