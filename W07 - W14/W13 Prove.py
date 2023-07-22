# W13 Prove assignment.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Create a program to calculate the wind chill.

# 1st Core:

wind_speed = 0

def compute_wind_chill(temp):
   return 35.74 + (0.6215 * float(temp)) - 35.75 * (float(wind_speed) ** 0.16) + 0.4275 * float(temp) * (float(wind_speed) ** 0.16)

def temp_to_fahrenheit(temp):
    return temp * 9/5 + 32

temp = float(input('What is the temperature? '))
temp_type = input('Fahrenheit or Celsius [F/C]? ')

if temp_type.lower() == 'c':
    temp = temp_to_fahrenheit(temp)

while wind_speed < 60:
    wind_speed += 5
    wind_chill = compute_wind_chill(temp)
    print(f'At temperature {temp:.2f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F')
