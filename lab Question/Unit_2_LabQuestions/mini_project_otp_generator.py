# Mini Project: OTP Generator
import random


def generate_otp(length=6):
    otp = ""
    for _ in range(length):
        otp += str(random.randint(0, 9))
    return otp


otp = generate_otp()
print("Your OTP is:", otp)

tries = 3
while tries > 0:
    entered = input("Enter the OTP: ")
    if entered == otp:
        print("OTP verified successfully!")
        break
    tries -= 1
    print("Wrong OTP. Attempts left:", tries)
else:
    print("Verification failed.")
