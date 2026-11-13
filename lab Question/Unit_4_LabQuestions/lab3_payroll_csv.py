# Lab Exercise 3: CSV-based payroll management system
import csv
import os

folder = os.path.dirname(__file__)
input_file = os.path.join(folder, "employees.csv")
output_file = os.path.join(folder, "payroll.csv")

try:
    with open(input_file, "r") as f:
        employees = list(csv.DictReader(f))
except FileNotFoundError:
    print("employees.csv not found.")
    employees = []

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "basic", "hra", "da", "pf", "net_salary"])

    print(f"{'ID':<6}{'Name':<10}{'Basic':>10}{'Net Salary':>14}")
    for emp in employees:
        basic = float(emp["basic_salary"])
        hra = basic * 0.20
        da = basic * 0.10
        pf = basic * 0.12
        net = basic + hra + da - pf
        writer.writerow([emp["id"], emp["name"], basic, hra, da, pf, net])
        print(f"{emp['id']:<6}{emp['name']:<10}{basic:>10.2f}{net:>14.2f}")

print("\nPayroll saved to payroll.csv")
