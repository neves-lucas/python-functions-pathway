# W07 Prove Activity.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Create a Wordle puzzle.

from os import system as clean

secret_word = "moriancumer"
attempts = 0

while True:
    guess = input("What is your guess? ")
    for letter in secret_word:
        if letter.lower() == guess.lower():
            print("_", end="")
        else:
            print(letter.lower(), end="")

        # if guess.lower() == "moriancumer":
        #     clean("cls")
        #     print("Congratulations! That is the right word. ")
        #     print(f"You tried {attempts} times. ")
        #     break
        # else:
        #     clean("cls")
        #     attempts = attempts + 1
        #     print("Wrong input, try again ")
        #     print(f"Your hint is: ")
        #     print()

