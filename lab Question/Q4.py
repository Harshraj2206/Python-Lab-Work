# Accepting the details from the user.

Consumer_name = input("Enter the consumer name: ")
Consumer_ID = input("Enter the consumer number: ")
prev_meter_reading = float(input("Enter the previous meter reading: "))
curr_meter_reading = float(input("Enter the current meter reading: "))
cost_perUnit = float(input("Enter the cost per unit: "))

# Calculate
Total_units_consumed = curr_meter_reading - prev_meter_reading
Energy_charge = Total_units_consumed * cost_perUnit

# 5% of energy charge
Electricity_duty = 0.05 * Energy_charge

#fixed charge = 100
fixed_meter_charge = 100

net_bill = Energy_charge + Electricity_duty + fixed_meter_charge
print("Consumer name:", Consumer_name)
print("Consumer ID:", Consumer_ID)
print("Total units consumed:", Total_units_consumed)
print("Energy charge:", Energy_charge)
print("Electricity duty:", Electricity_duty)
print("Fixed meter charge:", fixed_meter_charge)
print("Net bill:", net_bill)

    