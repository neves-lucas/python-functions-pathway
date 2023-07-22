# W02 Prove Assignment.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Create a "MadLib" type of program.

# Some inputs to build up the story. "Separation" have one clear purpose.
separation = '---------------------------------------------------------------------------------'
adjective = input('Adjective: ')
animal = input('Animal: ')
adjective2 = input('Adjective: ')
verb1 = input('Verb: ')
exclamation = input('Exclamation: ')
fruit = input("Fruit: ")
verb2 = input('Verb: ')
noun = input('Noun: ')
plural_noun = input('Plural noun: ')
verb3 = input('Verb: ')
name = input('Your name: ')

# I putted everything in one print statement, but it have line breaks.
print('\nFunny Storyteller!')
print(separation)
print(f'The other day, i was really in trouble. It all started after i ate some {fruit.lower()} \nwhen i saw a very {adjective.lower()} {animal.lower()} {verb1.lower()} down the hallway. "{exclamation.capitalize()}"! I yelled. \nBut all I could think to do was to {verb2.lower()} over and over. Miraculously, that caused it to stop, \nbut not before it tried to {verb3.lower()} right in front of my family. They were shocked and asked \n"{name.capitalize()}, why did you feared your {animal.lower()}? Now he will not eat the {fruit.lower()} we bought yesterday." \nNot knowing that the {fruit.lower()} i ate was from the {animal.lower()}, i just said "sorry" and went to my work. \nIt all was so crazy that i thought what could happen if i {verb2.lower()}in front of my teammates. \nAs a result, many of them where confuse and {verb1.lower()}.')
print(separation)