# Mini Project (Lab 4): Retail Sales Dashboard Using CSV and Matplotlib
import csv
import matplotlib.pyplot as plt

date_sales = {}
product_sales = {}

f = open("sales.csv", "r")
reader = csv.DictReader(f)
for row in reader:
    date = row["Date"]
    product = row["Product"]
    sales = int(row["Sales"])

    if date in date_sales:
        date_sales[date] = date_sales[date] + sales
    else:
        date_sales[date] = sales

    if product in product_sales:
        product_sales[product] = product_sales[product] + sales
    else:
        product_sales[product] = sales
f.close()

print("Daily total sales:")
for date in date_sales:
    print(date, ":", date_sales[date])

print("\nProduct-wise total sales:")
for product in product_sales:
    print(product, ":", product_sales[product])

plt.figure(figsize=(10, 4))

# line graph of daily sales
plt.subplot(1, 2, 1)
plt.plot(list(date_sales.keys()), list(date_sales.values()), marker="o")
plt.title("Daily Sales")
plt.xlabel("Date")
plt.ylabel("Sales")

# bar chart of product sales
plt.subplot(1, 2, 2)
plt.bar(list(product_sales.keys()), list(product_sales.values()))
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()
