# Lab Exercise 1: Contact book using lists and dictionaries

contacts = []

while True:
    print("\n1. Add  2. View  3. Search  4. Delete  5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        contacts.append({"name": name, "phone": phone, "email": email})
        print("Contact added.")

    elif choice == "2":
        if not contacts:
            print("No contacts.")
        for c in contacts:
            print(c["name"], "-", c["phone"], "-", c["email"])

    elif choice == "3":
        name = input("Enter name to search: ")
        found = False
        for c in contacts:
            if c["name"].lower() == name.lower():
                print(c["name"], "-", c["phone"], "-", c["email"])
                found = True
        if not found:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to delete: ")
        for c in contacts:
            if c["name"].lower() == name.lower():
                contacts.remove(c)
                print("Contact deleted.")
                break
        else:
            print("Contact not found.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
