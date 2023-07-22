# W06 Team Activiy.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Write a program for a fictitious amusement park ride.

from os import system as clean
approval = False
clean("cls")

rider1_age = int(input("What is the first rider's age? "))
rider1_height = int(input("What is the first rider's height? "))
passenger = input("There is a second rider? [Y/N]\n")

while True:
    clean("cls")
    while True:
        if passenger.lower() == "n" and rider1_age <= 12:
            golden_pass = input("Does this rider have a golden passport? [Y/N]\n")
            if golden_pass.lower() == "y":
                rider1_age = 18
            elif rider1_age >= 18 and rider1_height >= 62:
                approval = True
                break
            elif rider1_age < 18 or rider1_height < 36:
                approval = False
                break
            else:
                approval = False
                break
        elif passenger.lower() == "y":
            rider2_age = int(input("What is the second rider's age? "))
            rider2_height = int(input("What is the second rider's height? "))
            if rider2_age <= 12:
                golden_pass2 = input("Does this rider have a golden passport? [Y/N]\n")
                while True:
                    if golden_pass2.lower() == "y":
                        rider2_age = 18
                    elif rider1_age >= 18 or rider2_age >= 18 or golden_pass.lower() == "y" or golden_pass2.lower() == "y":
                        approval = True
                    elif rider1_age < 18 or rider2_age <18:
                        if rider1_age >= 16 and rider2_age >= 14:
                            approval = True
                        elif rider2_age >= 16 and rider1_age >= 14:
                            approval = True
                        else:
                            approval = False
                    elif rider1_height >= 52 and rider2_height >= 52 and rider1_age >= 12 and rider2_age >= 12:
                        approval = True
                        break
                    elif rider1_height < 36 or rider2_height < 36:
                        approval = False
                        break
                    elif rider1_age >= 18 and rider1_height >= 62:
                        approval = True
                        break
                    elif rider2_age >= 18 and rider2_height >= 62:
                        approval = True
                        break
                    else:
                        approval = False
                        break
            
        else:
            print("Wrong input.")
            break
    break
if approval:
    print("Approved.")
else:
    print("Rejected.")