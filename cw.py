# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * factorial(n-1)

# n = int(input("Enter your number habibi: "))
# print(f"The value of {n}! is:",factorial(n))



# def mult(num):
#     if num < 10:
#         return num
#     return (num%10) * mult(int(num/10))
# print(mult(785))



# def fibonacci(num):
#     if num == 0 or num == 1:
#         return num
#     return fibonacci(num -1) + fibonacci(num - 2)
# num = int(input("Enter number of terms: "))
# for i in range(num):
#     print(fibonacci(i), end=" ")



# add = lambda x1, x2 : x1 + x2
# x1 = int(input("Enter the first number: "))
# x2 = int(input("Enter the second number: "))
# print(add(x1, x2))



# square = lambda x : x*x
# print(square(5))


# import random
# num = random.randint(1, 1000)
# print(num)
# print(random.randrange(2, 10, 2))
# otp = random.randint(100000, 999999)
# print(otp)



# list1 = ["Hi", 1, True]
# print(list1)

# list2 = list((1, "Hello", False, 5))
# print(list2)

# sub = "HTML"
# list3 = list(("HTML", ))
# list4 = list(sub)
# print(list3)

# n = [ 1, 2, 3, 4, 5]
# n[1:3] = [7, 8, 9, 10]
# print(n)



# students = ["Harsh", "Jeel", "Kavya"]
# print(students)
# students.append("Gagan")
# print("list after we append:", students)
# students.insert(0, "Harsh Raj")
# print("after inserting new info:", students)



my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))

list1 = list(my_tuple)
print(list1)
print(type(list1))

list2 = [22, 23, 24, 25]
tuple2 = tuple(list2)
print(tuple2)
print(type(tuple2))

