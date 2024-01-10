from random import randint

while True:
    lower = input(f"Enter the lower bound: ")
    if lower != "exit":
        lower = int(lower)
        higher = int(input(f"Enter the upper bound: "))
        print(randint(lower, higher))
    else:
        break