# W11 Team Activity.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Develop a human resources system using text files.

with open("hr_system.txt") as hr_list:
    for line in hr_list:
        parts = line.strip()
        parts = line.split(" ")
        name = parts[0]
        id_num = parts[1]
        title = parts[2]
        salary = float(parts[3])

        # Calculating the pay amount
        pay_amount = salary / 24

        # Compute engineering bonus
        if title.lower() == "engineer":
            pay_amount += 1000

        print(f"{name} (ID: {id_num}), {title} - R${pay_amount:.2f}")