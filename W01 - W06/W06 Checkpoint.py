# W06 Checkpoint.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Write a program to determine whether to loan money.

print("Please enter 1-10 integers numbers. ")
loan = int(input("How large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
payment = int(input("How large is your down payment? "))

if loan >= 5:
    if credit_history >= 7 and income >= 7:
        print("You have the loan. ")
    elif credit_history == 7 or income == 7 and payment == 5:
        print("You have the loan. ")
    else:
        print("You don't have the loan. ")
elif loan <5:
    if credit_history < 4:
        print("You don't have the loan. ")
    else:
        if income == 7 or payment == 7:
            print("You have the loan. ")
        elif income == 4 and payment == 4:
            print("You have the loan. ")
        else:
            print("You don't have the loean. ")
else:
    ""