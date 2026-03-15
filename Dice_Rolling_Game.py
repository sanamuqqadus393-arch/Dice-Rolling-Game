
import random

count = 0

while True:

    dice = int(input("How many dice do you want to roll? "))

    for i in range(dice):
        number = random.randint(1, 6)
        print("Dice", i+1, ":", number)
    count += 1
    print(f"you rolled the dice for {count} times")

    ch = input("Roll the dice? (y/n):")

    if ch.lower() == "y":
        continue
    elif ch.lower() == "n":
        print("Thanks for playing!")
        break
    else:
        print("invalid choice")
