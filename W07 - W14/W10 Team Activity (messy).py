# W09 Team Activity.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Practice using multiple lists.

from os import system as clean
from statistics import mean

accounts = []
balances = []

while True:
    account_name = str(input("What is the name of this account? "))
    if account_name.lower() != "quit":
        account_balance = float(input("What is the balance of this account? R$"))
        accounts.append(account_name.capitalize())
        balances.append(account_balance)
    elif account_name.lower() == "quit":
        print()
        for i, account_name in enumerate(accounts):
            print("Accounts information: ")
            print(f"{i}. {accounts[i]} - R${balances[i]}")
        print()
        print(f"Total: R${sum(balances)}")
        print(f"Average: R${sum(balances) / len(balances)}")
        print(f"Highest balance: {max(accounts[i])} - R${balances[i]}")
        update = str(input("Do you want to update an account? [yes/no] "))
        if update.lower() == "yes":
            change = int(input("What account index do you want to update? ")) - 1
            new_amount = int(input("What is the new amout? R$"))
            accounts[change] = new_amount
        for i, account_name in enumerate(accounts):
            print("Accounts information: ")
            print(f"{i}. {accounts[i]} - R${balances[i]}")
        else:
            pass   


        break
    else:
        pass
