# W07 Checkpoint.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Create a loop asking for a positive number entry.

from os import system as clean

clean("cls")
number = int(input("Please, type a positive number: "))

while number < 0:
    clean("cls")
    print("That is a negative number.")
    number = int(input("Please, type a positive number: "))

print(f"The number is {number}.")


# Second task: Create a loop to ask for candy until "yes" entry.

clean("cls")
candy = input("May i have a piece of candy? ")

while True:
    if candy.lower() == "no":
        candy = input("May i have a piece of candy? ")
    elif candy.lower() == "yes":
        clean("cls")
        print("Thank you. ")
        break
    else:
        clean("cls")
        print("Wrong input. ")
        break
