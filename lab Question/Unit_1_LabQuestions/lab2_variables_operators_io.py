# Lab Exercise 2: Programs using variables, operators, and input/output

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Arithmetic operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# Relational operators
print("a > b:", a > b)
print("a == b:", a == b)

# Logical operators
print("a > 0 and b > 0:", a > 0 and b > 0)
print("a > 0 or b > 0:", a > 0 or b > 0)

# Bitwise operators
print("a & b:", a & b)
print("a | b:", a | b)

# Assignment operator
a += 5
print("a after a += 5:", a)

# Built-in functions and formatting
print("Type of a:", type(a))
print("ID of a:", id(a))
print(f"Sum using f-string: {a + b}")
print("Sum using format(): {}".format(a + b))
