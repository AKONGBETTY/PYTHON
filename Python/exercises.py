import random

while True:
    user_input = input("Do you want to roll the dice? (yes/no): ")
    if user_input == "yes":
        dice_roll1 = random.randint(1, 6)
        dice_roll2 = random.randint(1, 6)
        print(f"You rolled {dice_roll1}, {dice_roll2}")
    elif user_input == "no":
        print("Maybe next time!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
# add through terminal
