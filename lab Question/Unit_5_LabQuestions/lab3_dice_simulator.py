# Lab Exercise 3: Dice simulator using random module
import random

dice = int(input("How many dice do you want to roll? "))

while True:
    total = 0
    for i in range(dice):
        roll = random.randint(1, 6)
        print("Dice", i + 1, ":", roll)
        total = total + roll
    print("Total:", total)

    again = input("Roll again? (y/n): ")
    if again != "y":
        print("Thanks for playing!")
        break
