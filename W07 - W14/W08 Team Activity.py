# W08 Team Activity.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Practice iterating through strings.

word = "Commitment"

chosen_letter = input("What is one letter that you like? ")

# Core requirements.

# for letter in word:
#     if letter.lower() == chosen_letter.lower():
#         print(letter.upper(), end="")
#     else:
#         print(letter.lower(), end="")
# print()

# for letter in word:
#     if letter.lower() == chosen_letter.lower():
#         print("_", end="")
#     else:
#         print(letter.lower(), end="")
# print()

# Stretch challenges.

quote = "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough."

run_again = "yes"

while run_again == "yes":
    user_number = int(input("Please enter a number: "))

    for i, letter in enumerate(quote):
        if i% user_number ==0:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")

    print()
    run_again = input("Would you like to enter another number? ")

print("Goodbye.")
