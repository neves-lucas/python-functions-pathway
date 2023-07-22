import math

def area_square(side):
    return side * side

def area_rectangle(length, width):
    return length * width

def area_circle(radius):
    return radius * radius * math.pi

shape = ''

while shape != 'quit':
    shape = input('What shape do you have? ')

    shape = shape.lower()

    if shape == 'square':
        side = float(input('What is the length of one side? '))
        area = area_square(side)
        print(f'The area is {area}')

    if shape == 'circle':
        radius = float(input('What is the radius? '))
        area = area_circle(radius)
        print(f'The area is {area}')

    if shape == 'rectangle':
        length = float(input('What is the length? '))
        width = float(input('What is the width? '))
        area = area_rectangle(length, width)
        print(f'The area is {area}')