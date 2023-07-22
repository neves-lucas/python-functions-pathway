# W12 Team Activity.

# Name: Lucas Neves Rocha.
# Course: Programming building blocks.
# Instructor: Travis Christiansen.

# Task: Find items in a file.

# Here are some variables so we can find the maximum values


largest_chapters = -1
largest_book = ""

choice = input("Choose a section.")

with open("books_and_chapters.txt") as list:   # Core 1
    for lines in list:
        clean_line = lines.strip()

        part = clean_line.split(":")
        books = part[0]
        chapters = int(part[1])
        scripture = part[2]

        if scripture.lower() == choice.lower():
            print(f"Scripture: {scripture}, Book: {books}, Chapters: {chapters}")
            
            if chapters > largest_chapters:

                largest_chapters = chapters
                largest_book = books


        print(f"The book with the most chapters is: {largest_book}")
        print(f"It has {largest_chapters}")