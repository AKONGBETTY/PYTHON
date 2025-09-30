import random

random_number = random.randint(1, 10)
try:
    user_guess = int(input("Enter a number between 1 and 10: "))
except ValueError:
    print("Invalid input! Please enter a valid integer.")
if user_guess == random_number:
    print("correct")
elif user_guess < 1 or user_guess > 10:
    print("enter a value within range")
elif user_guess > random_number:
    print("go lower")
else:
    print("go higher")
