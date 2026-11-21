# Lab Exercise 2: Library management system

class Library:
    def __init__(self):
        self.books = {}  # book name -> "Available" or "Issued"

    def add_book(self, name):
        self.books[name] = "Available"
        print("Book added.")

    def show_books(self):
        for name in self.books:
            print(name, "-", self.books[name])

    def issue_book(self, name):
        if name not in self.books:
            print("Book not found.")
        elif self.books[name] == "Issued":
            print("Book is already issued.")
        else:
            self.books[name] = "Issued"
            print("Book issued:", name)

    def return_book(self, name):
        if name in self.books and self.books[name] == "Issued":
            self.books[name] = "Available"
            print("Book returned:", name)
        else:
            print("Invalid return.")


library = Library()

while True:
    print("\n1. Add Book  2. Show Books  3. Issue Book  4. Return Book  5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        library.add_book(input("Enter book name: "))
    elif choice == "2":
        library.show_books()
    elif choice == "3":
        library.issue_book(input("Enter book name to issue: "))
    elif choice == "4":
        library.return_book(input("Enter book name to return: "))
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
