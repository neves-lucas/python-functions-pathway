# Practice working with indexes

items = []

while True:
    item = str(input("Type the items for the shopping list: (Type \"quit\" to finish): ")).capitalize()
    if item.lower() != "quit":
        items.append(item)
    elif item.lower() == "quit":
        for i, item in enumerate(items):
            i += 1
            print(f"{i}. {item}")
        change = int(input("What is the item that you want to change? (number): ")) - 1
        new_item = str(input("What is the new item? ")).capitalize()
        items[change] = new_item

        for i, item in enumerate(items):
            i += 1
            print(f"{i}. {item}")
        break            

            

            
        