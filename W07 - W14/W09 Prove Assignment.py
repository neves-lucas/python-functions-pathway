# W09 Team Activity.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Create a shopping cart.

from os import system as clean
from time import sleep

# Variables

items = []
prices = []
item = ""
price = ""
choice = ""
menu = '''Welcome to the shopping cart system!
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
Choose an option: '''


clean('cls')
while True:
    clean('cls')
    choice = input(menu)
    if choice == "1":
        print()
        item = str(input("What is the name of the item? ").capitalize())
        price = str(input(f"What is the price of '{item}'? R$"))
        items.append(item)
        prices.append(price)
        print(f"'{item}' was added to your cart.")
        sleep(2)
    elif choice == "2":
        print()
        print("Your cart: ")
        for i in range(len(items)):
            print(f"{i}. {items[i]} - R${prices[i]}")
        print()
        choice = input("Press enter to go back to the menu.")
    elif choice == "3":
        print()
        change = int(input("Which item would you like to remove? "))
        items.remove(change)[change]
    elif choice == "5":
        print("Thank you, good bye. :)")
        sleep(2)
        clean("cls")
        break