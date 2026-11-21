# Lab Exercise 1: Bank account system using OOP

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)

    def show_balance(self):
        print(self.name, "balance:", self.balance)


name = input("Enter account holder name: ")
account = BankAccount(name, 1000)
print("Account created with opening balance 1000")

while True:
    print("\n1. Deposit  2. Withdraw  3. Balance  4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount: "))
        account.withdraw(amount)
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
