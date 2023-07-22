# W11 Prove assignment.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

'''Task: write a program to analyze a dataset containing information about life
 expectancies over the years throughout the countries of the world.
 '''

from os import system as clean

# General variables to make the program function
i = 0
lowest = 10000000
maximum = 1000
max_life = -1
min_life = 999999999999
choice = int(input("Enter a year: "))

with open("life-expectancy.csv") as dataset:
    whole_countries = []
    whole_years = []
    whole_lifexp = []


    for lines in dataset:
        clean_line = lines.strip()
        i += 1
        if i > 1:
            part = clean_line.split(",")
            country = part[0]
            code = part[1]
            year = int(part[2])
            life_expec = float(part[3])

            if year == choice:
                whole_countries.append(country)
                whole_years.append(year)
                whole_lifexp.append(life_expec)
                sum = 0

                for life_e in whole_lifexp:
                    sum += life_e
                    average = sum / len(whole_lifexp)


            # For max values
            if life_expec > max_life:
                max_life = life_expec
                max_country = country
                max_year = year

            # For min values
            elif life_expec > 0 and life_expec < min_life:
                min_life = life_expec
                min_country = country
                min_year  = year
    average = sum / len(life_expec)

    print(f"In {choice}: ")
    print(f"The average life expectancy was {average:.2f}")

    print(f"The overall max life expectancy is: {max_life:.2f} from {max_country} in {max_year}")
    print(f"The overall min life expectancy is: {min_life:.2f} from {min_country} in {min_year}")
