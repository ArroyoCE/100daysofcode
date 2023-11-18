import lib.art
import lib.game_data
import random
import os


def compare(a, b):
    if a > b:
        return True


alive = True
pick_a = random.choice(lib.game_data.data)
score = 0

while alive:
    os.system('cls')
    pick_b = random.choice(lib.game_data.data)
    print(lib.art.high)
    print(f"\nTotal Score:  {score}  \n")
    print(f"\n      Contestant A: {pick_a['name']}, {pick_a['description']}, from {pick_a['country']}")
    print(lib.art.vs)
    print(f"\n      Contestant B: {pick_b['name']}, {pick_b['description']}, from {pick_b['country']}")
    decision = input("\nWho has more followers? type 'A' or 'B': ")

    if decision.upper() == 'A':
        if compare(pick_a['follower_count'], pick_b['follower_count']) == True:
            print("Congratulations, you've guessed it right")
            pick_b = random.choice(lib.game_data.data)
            score += 1
            input("\n\nPress any button to start the next round.")
        else:
            alive = False
    else:
        if compare(pick_b["follower_count"], pick_a["follower_count"]) == True:
            print("\nCongratulations, you've guessed it right.")
            pick_a = pick_b
            pick_b = random.choice(lib.game_data.data)
            score += 1
            input("\n\nPress any button to start the next round.")
        else:
            alive = False


os.system('cls')
print(lib.art.high)
print("\nSorry, you guessed it wrong...")
print(f"\nYour total score was {score}")
input("\nPress any button to close.")
