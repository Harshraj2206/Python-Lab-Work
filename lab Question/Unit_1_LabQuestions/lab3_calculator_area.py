# Lab Exercise 3: Simple calculator and area calculation programs
import math

# Simple calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Result:", a / b)
else:
    print("Invalid operator")

# Area calculation
r = float(input("Enter radius of circle: "))
print("Area of circle:", round(math.pi * r * r, 2))

l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))
print("Area of rectangle:", l * w)

base = float(input("Enter base of triangle: "))
h = float(input("Enter height of triangle: "))
print("Area of triangle:", 0.5 * base * h)
