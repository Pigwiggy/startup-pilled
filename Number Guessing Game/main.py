import random
import numpy as np


x = random.randint(1, 100)
y = 0
counter = 0

while y < 1:
    guess = int(input("Enter your guess for a number between 1-100: "))
    counter += 1

    if guess > x:
        print("Your guess is too large, try again")
    elif guess < x:
        print("Your guess is too small, try again")
    elif guess == x:
        print("Correct!")
        print(f"That took you {counter} tries")
        break

