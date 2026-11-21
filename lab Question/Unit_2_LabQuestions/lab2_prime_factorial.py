# Lab Exercise 2: Prime number and factorial programs

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

print("Factorial of", num, "is", factorial(num))
