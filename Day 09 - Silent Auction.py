import os

print("""


                         ___________
                        \\         /
                          )_______(
                          |'''''''|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )'''''''(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\

""")

bidders = {}
print("\nWelcome to the secret auction program.\n")
while True:
    print("New bid information:")
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    bidders.update({bid: name})
    while True:
        decision = input("\nAre there any other bidders? Type 'yes' or 'no': ")
        if decision.lower() == 'yes' or decision.lower() == 'no':
            break
        else:
            print("Please type 'yes' or 'no'")

    if decision.lower() == 'no':
        break
    elif decision.lower() == 'yes':
        os.system('cls')

os.system('cls')
print(f"The winner is {bidders[max(bidders)]} with a bid of ${max(bidders)}")
