print()
grade = int(input("What is your grade percentage? "))
last_number = grade % 10

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
elif grade < 60:
    letter = "F"
else:
    print("Try again.")

# Stretch challenges.
sign = ""

if last_number >= 7:
    sign = "+"
elif last_number < 3:
    sign = "-"
else:
    sign = ""

if grade >= 93:
    sign = ""

if letter == "F":
    sign = ""

print(f"Your grade is: {letter}{sign}")

if grade >= 70:
    print("Congratulations! You passed.")
else:
    print("Sorry, your grade is not enough to pass. Don't give up, you'll do it next time.")