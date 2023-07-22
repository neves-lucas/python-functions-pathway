# # W04 Prove Assignment.

# # Name: Lucas Neves Rocha.
# # Course: Programming building blocks.
# # Instructor: Travis Christiansen.

# # Task: Compute the price of a child and adult meals.

# # Starting by the inputs to gather data. When asking about
# # money, we should always consider the possibility of having a
# # floating point number, so i included before the input itself.

from timeit import repeat
import math

separation = "-------------------------------------------------------------------------"
child_meal = float(input("What is the price of a child's meal? "))
child_num = int(input("How many children will eat? "))
child_drink = float(input("How much it costs what they will drink? "))
adult_meal = float(input("What is the price of an adult's meal? "))
adult_num = int(input("How many adults will eat? "))
adult_drink = float(input("How much it costs what they will drink? "))
tax = float(input("What is the sales tax? "))
print("")
print("There is also a 10% tip percentage. ")

# Variables to do the math.
child_total = child_meal + child_drink * child_num
adult_total = adult_drink + adult_meal * adult_num
total_sum = child_total + adult_total
tip = 10/100
tip_total = total_sum * tip
sales_tax = total_sum * tax / 100 + tip
final_sum = sales_tax + tip_total + total_sum
credit_fee = (0.5/100) * final_sum
required_number = final_sum + credit_fee

# The program.
print("The children's meal subtotal is $" + str(child_total))
print("The adult's meal subtotal is $" + str(adult_total))
print("Together, the meals are $" + str(total_sum))
print("")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Tip: ${tip_total:.2f}")
print(f"Total price after the tax and the tip: ${final_sum:.2f}")
print("")
payment_method = input("Choose the payment method:\n1. Credit Card. (+0.5% fee)\n2. Debit Card.\n3. Money.\n")
print("")

# Boolean decision. If the user chooses credit card, there is an additional fee.
if payment_method == "1":
    print(f"New price: ${credit_fee + final_sum:.2f}")
    payment = float(input("What is the payment amount? $"))
    
while payment < required_number:
        print("Not enough money. Please, insert the right amount.\n")
        payment = float(input("What is the payment amount? $"))
if float(payment) > required_number:
        change = payment - required_number
        print(f"Change: ${change:.2f}")
        print("Thank you for the preference! :)")
else:
        ""
 