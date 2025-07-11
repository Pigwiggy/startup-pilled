import random
import numpy as np
import pandas as pd
import matplotlib
import time


with open('Word Guessing Games/WordleLite/words.txt', 'r') as file:
    words = [line.strip() for line in file]
word = random.choice(words)
# For debugging: print(word)

print("Welcome to WordleLite, you have 6 tries to guess a 5-letter word")
tries_left = 6


while tries_left > 0:

    guess = input("Guess a 5 letter-word: ").strip().lower()

    # Tells user they got the correct answer
    if guess == word:
        print(f"Correct! The word is {word}")
        break

    # Checks if user input is five letters or contains non-alphabetical letters
    if len(guess) != 5:
        print("The word needs to be 5 letters: ")
        print(f"You have {tries_left} guesses left")
    elif not guess.isalpha():
        print("Enter alphabetical letters only: ")
        print(f"You have {tries_left} guesses left")
    
    # Identifies correct letters, misplaced letters, and incorrect letters from the user's guess
    else:
        misplaced_letters = []
        feedback = ""

        letters = []
        for i in word:
            letters.append(i)

        for i in range(len(guess)):
            if guess[i] != word[i]:
                feedback += "_"
                if guess[i] in letters:
                    misplaced_letters.append(guess[i])
                    letters.remove(guess[i])
            elif guess[i] == word[i]:
                feedback += f"{guess[i]}"

        print(f"Here are the letters you got in the right position: {feedback}")
        print(f"Here are the letters you got right but in the wrong place: {misplaced_letters}")
        tries_left -= 1
        if tries_left == 1:
             print(f"You have {tries_left} guess left")
        else:
            print(f"You have {tries_left} guesses left")


print("Game over")
print(f"The word was {word}")


    