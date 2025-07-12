import random
import numpy as np
import matplotlib
import time

def easy_mode(slur):
    # For debugging: print(slur)
    print(f"The slur has {len(slur)} letters")
    
    # Determine number of tries given to user based on word length
    tries_left = len(slur) + 1
    try_counter = 0
    print(f"You have {tries_left} guesses")

    while tries_left > 0: 
        guess = input("Guess the slur: ").strip().lower()
        try_counter += 1

        # If user guesses correctly
        if guess == slur:
            print(f"Correct! The slur was {slur}")
            print(f"That took you {try_counter} guesses")
            break

        # Verifies user input length and character type
        if len(guess) != len(slur):
            print(f"The slur has {len(slur)} letters")
            if tries_left == 1:
                print(f"You have {tries_left} guess left")
            else:    
                print(f"You have {tries_left} guesses left")
        elif not guess.isalpha():
            print("Please only enter alphabetical letters")
            if tries_left == 1:
                print(f"You have {tries_left} guess left")
            else:    
                print(f"You have {tries_left} guesses left")

        # Feedbacks to the user which letters they got right and which ones are in the wrong position
        else:
            misplaced_letters = []
            feedback = ""

            letters = []
            for i in slur:
                letters.append(i)

            for i in range(len(guess)):
                if guess[i] != slur[i]:
                    feedback += "_"
                    if guess[i] in letters:
                        misplaced_letters.append(guess[i])
                        letters.remove(guess[i])
                elif guess[i] == slur[i]:
                    feedback += f"{guess[i]}"

            print(f"Here are the letters you got in the right position: {feedback}")
            print(f"Here are the letters you got right but in the wrong place: {misplaced_letters}")
            tries_left -= 1
            if tries_left == 1:
                print(f"You have {tries_left} guess left")
            else:
                print(f"You have {tries_left} guesses left")

    print("Game over!")
    print(f"The slur was {slur}")



def hard_mode(slur):
    print(slur)
    if len(slur) <= 4:
        tries_left = 5
    elif len(slur) >= 5 and len(slur) < 7:
        tries_left = 7
    elif len(slur) >= 7 and len(slur) < 9:
        tries_left = 8
    else:
        tries_left = 10

    try_counter = 0
    while tries_left > 0:
        guess = input("Guess the slur: ").strip().lower()
        try_counter += 1
        right_place = 0

        # If user guesses correctly
        if guess == slur:
            print(f"Correct! The slur was {slur}")
            print(f"That took you {try_counter} guesses")
            break

        # Verifies user's input as alphabetical letters    
        if not guess.isalpha():
            print("Please only enter alphabetical letters")

        # Feedbacks to the user which letters they got right and which ones are in the wrong position
        else:
            misplaced_letters = []
            feedback = ""
            for i in slur:
                feedback += "_"
            letters = []
            for i in slur:
                letters.append(i)


            for i in range(len(guess)):
                if i == len(slur):
                    break
                if guess[i] != slur[i] and guess[i] in letters:
                    misplaced_letters.append(guess[i])
                    letters.remove(guess[i])
                elif guess[i] == slur[i]:
                    feedback = feedback[:i] + guess[i] + feedback[i+1:]
                    right_place = 1


            # The length of the word will only be revealed for guesses where the user gets the right letter in the right place
            if right_place == 1:
                print(f"Here are the letters you got in the right position: {feedback}")

            print(f"Here are the letters you got right but in the wrong place: {misplaced_letters}")
            tries_left -= 1
            if tries_left == 1:
                print(f"You have {tries_left} guess left")
            elif tries_left <= 3:
                print(f"You have {tries_left} guesses left")

    print("Game over!")
    print(f"The slur was {slur}")



def main():
    with open('Word Guessing Games/Slurdle/slurbank.txt', 'r') as file:
        slurs = [line.strip() for line in file]
    slur = random.choice(slurs).strip().lower()
    # For debugging: print(slur)

    check = 0
    while check < 1:
        
        gamemode = input("Welcome to Slurdle, please choose by typing if you want to play the \"easy\" or \"hard\" mode: ").strip().lower()
        
        if gamemode == "easy":
            easy_mode(slur)
            break
        elif gamemode == "hard":
            hard_mode(slur)
            break
        else:
            print("Not a valid gamemode, please type \"easy\" or \"hard\"")

main()