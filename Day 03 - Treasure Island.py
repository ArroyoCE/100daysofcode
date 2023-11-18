print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island!")
print("Your mission is to find the treasure")
direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n" )
if direction.lower() == "left":
    direction = input("You come across a river, it is dark, do you wait for sunrise or swim across? type \"swim\" or \"wait\"\n" )
    if direction.lower() == "wait":
        direction = input("Waiting proves wise. At sunrise you can see the treacherous nature of the river, crossing would be deadly. You start walking along the river and come across a castle, with three doors for entrances, which door will you choose? Type \"red\", \"yellow\" or \"blue\"\n")
        
        if direction.lower() == "yellow":
            print("That's it! You have arrived at the safe haven. Game Won!") 
            input("Press any button to end game.") 
        elif direction.lower() == "red":
            print("There is only fire waiting for you. Game Over!") 
            input("Press any button to end game.")
        else:
            print("You should have made a wiser choice, you've been eaten by beasts. Game Over!") 
            input("Press any button to end game.")            
    else:
        print("You cannot make it, you are too weak. Game Over.\n\n")
        input("Press any button to end game.")    

else:
    print("You've made your choice, now you are surrounded by bandits, they murder you and take everyone of your belongings. Game Over.\n\n")
    input("Press any button to end game.")
    
        