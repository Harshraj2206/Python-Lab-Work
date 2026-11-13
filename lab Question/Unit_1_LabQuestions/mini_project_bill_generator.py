# Mini Project: Bill Generator

customer = input("Enter customer name: ")
n = int(input("Enter number of items: "))

total = 0
bill = ""
for i in range(n):
    item = input(f"Item {i + 1} name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    amount = price * qty
    total += amount
    bill += f"{item:<15}{price:>10.2f}{qty:>6}{amount:>12.2f}\n"

gst = total * 0.18
grand_total = total + gst

print("\n----------- BILL -----------")
print("Customer:", customer)
print(f"{'Item':<15}{'Price':>10}{'Qty':>6}{'Amount':>12}")
print(bill, end="")
print(f"Subtotal: {total:.2f}")
print(f"GST (18%): {gst:.2f}")
print(f"Grand Total: {grand_total:.2f}")
