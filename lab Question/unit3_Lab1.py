contacts = []

while True:
    print("\n1. Add a contact")
    print("2. Display all the contact")
    print("3. Search")
    print("4. Delete contact")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Add a contact
    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contact = {
            "name": name,
            "phone": phone,
        }

        contacts.append(contact)
        print("Contact added..")

    # Display all contacts
    elif choice == 2:
        if len(contacts) == 0:
            print("No contact is added to the book.")

        else:
            for contact in contacts:
                print("\nName:", contact["name"])
                print("Phone:", contact["phone"])

    # Search contact
    elif choice == 3:
        name = input("Enter the name: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                print("\nContact Found!")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])

                found = True
                break

        if not found:
            print("Contact not found.")

    # Delete contact
    elif choice == 4:
        name = input("Enter the name of the contact to delete: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break

        if not found:
            print("Contact not found.")

    # Exit
    elif choice == 5:
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice. Please try again.")