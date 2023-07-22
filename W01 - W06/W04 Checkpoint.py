# W04 Checkpoint Activity.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Write a program to convert from Fahrenheit to Celsius. Display the result to one decimal place of precision.

# Input to gather data
import math

temperature_f = float(input("What is the temperature in Fahrenheit? "))

# Variable to the math process
temperature_c = (temperature_f - 32) * 5/9

# Output
print(f"The temperature in Celsius is {temperature_c:.1f} degrees.")