# Mini Project: Bill Generator

customer = input("Enter customer name: ")
n = int(input("Enter number of items: "))

total = 0
bill = []
for i in range(n):
    item = input("Enter item name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    amount = price * qty
    total = total + amount
    bill.append([item, price, qty, amount])

gst = total * 0.18
grand_total = total + gst

print("\n----------- BILL -----------")
print("Customer:", customer)
print("Item  Price  Qty  Amount")
for b in bill:
    print(b[0], b[1], b[2], b[3])
print("Subtotal:", total)
print("GST (18%):", round(gst, 2))
print("Grand Total:", round(grand_total, 2))
