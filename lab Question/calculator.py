num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operand = input("Select your operands: ")

if operand == "+":
    print(num1 + num2)

elif operand == "-":
    if num1 > num2:
        print(num1 - num2)
    else :
        print(num2 - num1)

elif operand == "*":
    print(num1 * num2)

elif operand == "/":
    if num1 > num2:
        print(num1/num2)
    else:
        print(num2/num1)


