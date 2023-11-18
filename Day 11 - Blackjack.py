import lib.art
import lib.deck
import random
import os


card_pool = lib.deck.cards


def fresh():
    os.system('cls')
    print(lib.art.blackjack)



def deal():
    pick = random.choice(card_pool)
    for items in card_pool:
        if pick == items:
            del card_pool[card_pool.index(pick)]
            return pick


def resolve_computer():
    if sum(computer) < 17:
        computer.append(deal())
        resolve_computer()


def check(hand):
    if sum(hand) > 21:
        for item in hand:
            if item == 11:
                hand[hand.index(11)] = 1
    return sum(hand)


def check_winner():
    print(f"Your final hand: {player}, final score: {check(player)}")
    print(f"Computer's final hand: {computer}, final score: {check(computer)}")
    if check(player) == check(computer):
        return "Draw 🙃"
    elif check(player) > check(computer) or check(computer) > 21:
        return "You win!!"
    else:
        return "You lose!"


fresh()
count = 0
draw = input("Do you wish to play a hand? Type 'y' or 'n'\n")

while count < 4 and draw == 'y':
    player = []
    computer = []
    player.append(deal())
    computer.append(deal())
    while draw == 'y':
        player.append(deal())

        if check(player) > 21:
            draw = "n"
            resolve_computer()
            break
        fresh()

        print(f"     Your cards: {player}, current score {check(player)}")
        print(f"     Computer's first card: {computer[0]}")



        draw = input("\nType 'y' to get another card, type 'n' to pass: ")

        if draw == 'n':
            resolve_computer()
    count += 1
    fresh()
    if check(player) > 21:
        print(f"Your final hand {player}, final score {check(player)}")
        print("You went over. You lose 😭")
    else:
        print(check_winner())


    draw = input("\nDo you want to play again? type 'y' or 'n'\n")
