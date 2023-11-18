from random import randint

def main ():
    while True:
        try:
            choice = int(input("What do you choose?\nType:\n0 - Rock\n1 - Paper\n2 - Scissors\n"))
            if choice < 0 or choice >2:
                print("Please, use a number between 0 and 2.")
                input() 
            else: 
                break    
        
        except ValueError:
            print("Please use a number.")
            input()
    print("\nYou chose:\n")   
    rockpaperscissors(choice)
    
    compchoice = randint(0, 2)
    
    print("\nComputer chooses:\n")
    rockpaperscissors(compchoice)
    
    if (compchoice == 0 and choice == 2) or (compchoice == 1 and choice == 0) or (compchoice == 2 and choice == 1):
        print("\nVocê Perdeu!!")
    elif compchoice == choice:
        print("Empate!")
    else:
        print("Você ganhou!!!")
        
    input()            
    
            

def rockpaperscissors(choice):    
    if choice == 0:
        return print("""
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
        """)
    elif choice == 1:
        return print("""
            _______
        ---'    ____)____
                ______)
                _______)
                _______)
        ---.__________)
        """)
    else:
        return print("""
            _______
        ---'   ____)____
                ______)
            __________)
            (____)
        ---.__(___)
        """)        
   
main()            