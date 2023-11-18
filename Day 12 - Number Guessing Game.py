import random
import os


def guess(number, chance):
    print(f"You have {chance} attempt(s) remaining to guess the number.")
    choice = int(input("Make a guess: "))
    if choice > number:
        print("Too high!")
    elif choice < number:
        print("Too low!")
    else:
        print("You've guessed it right!! Congratulations!")
        input("\nPress any key to exit.")
        exit()
    chance -= 1
    if chance > 0:
        print("Guess again!")
        input("\nPress any key to continue.")

    return chance


random_number = random.choice(range(1, 101))
chances = 0
while chances == 0:
    os.system('cls')
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("\n\nChoose a difficulty. Type 'easy' or 'hard'\n").lower()

    if difficulty == 'easy':
        chances = 10

    elif difficulty == 'hard':
        chances = 5

while chances > 0:
    os.system('cls')
    chances = guess(random_number, chances)

print(f"Your chances are over!\nThe selected number was: {random_number}")
input("\nPress any key to exit.")
exit()
