member = input("Enter a new member: ").title()

file = open("members.txt", "a")
file.write(f"{member}\n")
file.close()

file = open("members.txt", "r")
members = file.readlines()
for member in members:
    print(member)
file.close()