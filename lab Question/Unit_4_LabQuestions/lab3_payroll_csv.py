# Lab Exercise 3: CSV-based payroll management system
import csv

infile = open("employees.csv", "r")
outfile = open("payroll.csv", "w", newline="")

reader = csv.DictReader(infile)
writer = csv.writer(outfile)
writer.writerow(["id", "name", "basic", "hra", "da", "pf", "net_salary"])

print("ID  Name  Basic  Net Salary")
for emp in reader:
    basic = float(emp["basic_salary"])
    hra = basic * 0.20
    da = basic * 0.10
    pf = basic * 0.12
    net = basic + hra + da - pf
    writer.writerow([emp["id"], emp["name"], basic, hra, da, pf, net])
    print(emp["id"], emp["name"], basic, net)

infile.close()
outfile.close()
print("\nPayroll saved to payroll.csv")
