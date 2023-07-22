# W09 Team Activity.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Practice using lists.

# here are the initial variables.
numbers = []
new_number = ""
numbers_total = 0

# 1st Core: Compute the sum.
while new_number != 0:
    new_number = int(input("Enter a number: "))
    if new_number != 0:
        numbers.append(new_number)
        numbers_total += new_number


# 2nd and 3rd Core: Compute the average and find the maximum.
average = float(sum(numbers)) / float(len(numbers))
largest_number = max(numbers)

# 1st Stretch challenge
maybe_smallest_number = 9999999999999

for number in numbers:
    if number > 0 and number < maybe_smallest_number:
        maybe_smallest_number = number

# 2nd Stretch challenge
sorted_list = sorted(numbers)


print(f"The total is: {numbers_total}.")
print(f"The average of the numbers is: {average}")
print(f"The largest number is: {largest_number}")
print(f"The smallest positive number is: {maybe_smallest_number}")
print("Your sorted list is: ")

for number in sorted_list:
    print(number)