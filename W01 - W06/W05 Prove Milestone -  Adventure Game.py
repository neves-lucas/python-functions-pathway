# W05 Prove Assignment.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Create a text-type adventure game.
from sys import exit
from os import system as clear

clear("cls")
name = input("What is your name?\n")

# The input "start" asks if the user wants to participate of the assignment.
# While is used so eveything else that is not Y or N will be rejected.
# I used "clear" to keep the terminal clean.

while True:
    clear("cls")
    while True:
        print(f"Well {name.capitalize()}, nice to meet you. My name is Lucas and i really need your help with something.")
        print()

        start = input("I have homework to do... It is about creating an Adventure Game with options or, \nbetter saying, paths to take. Could you help me? [Y/N]\n")
        if start.lower() == "n":
            clear("cls")
            print("No worries, i'll find someone else to help me. Anyways, thank you and have a great week! :)")
            break

        elif start.lower() == "y":
            clear("cls")
            print("Okay, let's move on.")
            print()
            break

        else:
            clear("cls")
            print("Wrong input, please answer with Y or N. ")
            print()

    if start.lower() == "n":
        break

    # Here is the first part of the program. The user can choose between two options.
  
    clear("cls")
    while True:
        decision = input("It is Monday. You wake up with fair enough time before work, \nbut you also have homework from college to do. What is the first thing to do? SCRIPTURE STUDY or HOMEWORK?\n")  
        if decision.lower() == "scripture study":
            clear("cls")
            print("You realize that by reading the scriptures and praying you'll have\nthe spirit to work on your assignments and have a good performance at your work.")

            # If the user types "scripture study" he/she will have another three options, but then the program ends.
            # If the user types anything else, the program doesn't work.

            while True:
                decision1_1 = input("Linear reading is always good, but you thoughtfully choose between 2 NEPHI, ALMA and ETHER.\n")
                if decision1_1.lower() == "2 nephi":
                    clear("cls")
                    print("You open the Book of Mormon and read, in 3 Nephi 32:3 that you should\n'feast upon the words of Christ' because 'the words of Christ will tell you all things what ye should do.'")
                    print("You realize that needs to be more diligent with scripture studies and plan to read them for at least 15 minutes every day before work.")
                    print()
                    break

                elif decision1_1.lower() == "alma":
                    clear("cls")
                    print("You open the Book of Mormon and read, in Alma 7:12 that Christ suffered to know how to help you according to your infirmities.")
                    print("By reading this scripture you grow your testimony about Christ's divine role in guide you through your decisions.")
                    print()
                    break

                elif decision1_1.lower() == "ether":
                    clear("cls")
                    print("You open the Book of Mormon and read, in Ether 12:27 that Christ 'give unto men weakness that they may\nbe humble' and that if you humble yourself before Him, He will make 'weak things become strong' to you.")
                    print("Then you realize that by being humble and asking His help to conciliate all the things you need to do, He would definatively strenghten you.")
                    print()
                    break
                else:
                    clear("cls")
                    print("Wrong input, try again.")
                    print()
            break

                # If the user choses "homework" the program continues.

        elif decision.lower() == "homework":
            clear("cls")
            print("You start to work on your college assignments but after 15 minutes gets distracted and\ncatch yourself watching random YouTube videos, wasting time.")
            print("When you realize, you ended up losing the entire morning and need to hurry up to your job,\nthus not reading the scriptures, neither doing your homework. ")
            print("")
            print("After being sad with yourself the whole day, you decide that when you arive home, you will take a serious study time.")

            # Another while to keeps the user typing what he/she should type on the last part of the program.

            while True:
                decision2 = input("You finally arive home. You're so tired after a whole day of hardwork,\nand even question yourself... 'i am going to STUDY or REST?'\n")
                if decision2.lower() == "study":
                    clear("cls") 
                    print("You take a cold shower, eat dinner and push yourself to focus and work on your assignments; thus finishing everything you needed to do by 11PM.")
                    print("Then you go to your bed and fall asleep.")
                    print()
                    print("You learned the lesson and never neglect your study time again. :)")
                    break

                elif decision2.lower() == "rest":
                    clear("cls")
                    print("You haven't learned the lesson... :(")
                    print("Thank you for participating!")
                    break
            
                else:
                    clear("cls")
                    print("Wrong input, try again.")
                    print()
            break
        else:
            clear("cls")
            print("Wrong input, try again.")
            print()
            
        
    break
