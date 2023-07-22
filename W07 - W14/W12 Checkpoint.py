    
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

# Write a program that finds the youngest person in the list.
min_age = 99999
min_person = ""
i = 1
for list in people:
    clean_list = list.strip()
    i += 1
    if i >= 1:
        parts = clean_list.split(" ")
        person = parts[0]
        ages = int(parts[1])
        if ages > 0 and ages < min_age:
            min_age = ages
            min_person = person

print(f"{parts[0]}, {parts[1]}")
print()
print(f"Youngest: {min_person}, age: {min_age}.")