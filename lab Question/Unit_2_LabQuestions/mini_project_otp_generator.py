# Mini Project: OTP Generator
import random

# make a 6 digit OTP
otp = ""
for i in range(6):
    otp = otp + str(random.randint(0, 9))

print("Your OTP is:", otp)

verified = False
for attempt in range(3):
    entered = input("Enter the OTP: ")
    if entered == otp:
        verified = True
        break
    print("Wrong OTP. Attempts left:", 2 - attempt)

if verified:
    print("OTP verified successfully!")
else:
    print("Verification failed.")
