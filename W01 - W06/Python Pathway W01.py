import colorama
from colorama import Fore
from tkinter.messagebox import YES


name = input("Hey, my name is Lucas. What's yours?\n")
print("")
print(f"Nice to meet you {name}, what is your favorite color?\n**Hint: try the primary and secondary colors, no cap letters.**")
print("")
color = input("")
if color == "blue":
    print(f"Violets are also {color}, aren't they?")
if color == "yellow":
    print(f"{color} just reminds me of McDonalds, hahaha.")
if color == "red":
    print("Like roses?")
if color == "green":
    print("Cool, do you have any leprechaun friend?")
if color == "orange":
    print("Citruslicious.")
if color == "violet":
    print("Not my favorite, but pretty.")
print(f"Awesome. Do you often wear clothes in {color}?")
answerClothes = input("")
if answerClothes == "yes":
    print("I can't see you, but it must be great.")
if answerClothes == "no":
    print("Got it.")
print("")
print("Well, i really like black, white and grey. Are my choices boring?")
answer = input("")
if answer == "yes":
    print("Sorry, i'm not a color person :( ... Well, nice to meet you!")
if answer == "no":
    print("Thank you! I really like the minimalistic asthetics... Well, nice to meet you!")
