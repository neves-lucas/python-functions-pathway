# Task: Practice working with lists.

friends = []
new_friend = ""

while new_friend != "end":
    new_friend = input("What is the name of your friend? ")
    if new_friend != "end":
        friends.append(new_friend)

print()
print("The names of your friends are: ")

for friend in friends:
    print(friend)