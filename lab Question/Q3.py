import math
num = float(input("Enter a number: "))

# square of the number
square = num**2
print("square:", square)

# cube of the number
cube = num**3
print("cube:", cube)

# square root of the number
square_root = math.sqrt(num)
print("square root:", square_root)

# ceiling value of the number
ceiling_value = math.ceil(num)
print("ceiling value:", ceiling_value)

# floor value of the number
floor_value = math.floor(num)   
print("floor value:", floor_value)

# absolute value of the number
absolute_value = abs(num)
print("absolute value:", absolute_value)

# type of the variable
variable_type = type(num)
print("type:", variable_type)

# memory address of the variable
memory_address = id(num)
print("memory address:", memory_address)

