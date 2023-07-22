# W03 Prove Assignment.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Compute the price of a child and adult meals.

# Starting by the inputs to gather data. When asking about
# money, we should always consider the possibility of having a
# floating point number, so i included before the input itself.

separation = "-------------------------------------------------------------------------"
childMeal = float(input("What is the price of a child's meal? "))
childNum = int(input("How many children will eat? "))
childDrink = float(input("How much it costs what they will drink? "))
adultMeal = float(input("What is the price of an adult's meal? "))
adultNum = int(input("How many adults will eat? "))
adultDrink = float(input("How much it costs what they will drink? "))
tax = float(input("What is the sales tax? "))
print("")
print("There is also a 10% tip percentage. ")

# Variables to do the math.
childTotal = childMeal + childDrink * childNum
adultTotal = adultDrink + adultMeal * adultNum
totalSum = childTotal + adultTotal
tip = 10/100
tipTotal = totalSum * tip
salesTax = totalSum * tax / 100 + tip
finalSum = salesTax + tipTotal + totalSum

# The program.
print(separation)
print("The children's meal subtotal is $" + str(childTotal))
print("The adult's meal subtotal is $" + str(adultTotal))
print("Together, the meals are $" + str(totalSum))
print("")
print(f"Sales tax: ${salesTax:.2f}")
print(f"Tip: ${tipTotal:.2f}")
print(f"Total price after the tax and the tip: ${finalSum:.2f}")
print("")
payment = float(input("What is the payment amount? $"))
change = payment - finalSum
if finalSum > payment:
    print("Sorry, you don't have enough money.")
else:
    print(f"Change: ${change:.2f}")
print(separation)