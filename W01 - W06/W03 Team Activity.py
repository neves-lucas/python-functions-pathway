# W03 Team Activity.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Write a program to compute the areas of three different shapes: Square, Circle and Rectangle.

# Area of the square.
from math import pi
separation = "---------------------------------------------------------------------------------------------"
print(separation)
length = float(input("Want to see a magic trick? Insert one value for length and i will\n show you the area of a square, a circle with that radius,\n the volume of a cube and a sphere with that radius."))
areaSquare = length*length
print("The area of the square is " + str(areaSquare))
print("")

# Area of the retangle.
rectangleWidth = float(input("What is the width of the rectangle? "))
areaRectangle = rectangleWidth * length
print("The area of the rectangle is " + str(areaRectangle))
print("")

#Area of the circle.
areaCircle = length ** 2 * pi
print("The area of the circle is " + str(areaCircle))
print("")

#Volume of the cube.
volumeCube = length ** 3
print("The volume of the cube is " + str(volumeCube))
print("")
