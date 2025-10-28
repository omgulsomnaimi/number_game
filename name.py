import random

print("Welcome to the Number Guessing Game 🎯")
number = random.randint(1, 10)

while True:
    guess = input("Guess a number between 1 and 10: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if guess == number:
        print("🎉 Correct! You guessed the number!")
        break
    else:
        print("❌ Wrong! Try again.")
