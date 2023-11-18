import random
from lib.dic import dictionary

print("  sSSs    sSSs_sSSs     .S_sSSs      sSSs   .S_SSSs\n"
     + "d%%SP   d%%SP~YS%%b   .SS~YS%%b    d%%SP  .SS~SSSSS\n"   
        +"d%S     d%S       S%b  S%S    S%b  d%S     S%S   SSSS\n"  
       + "S%S     S%S       S%S  S%S    S%S  S%S     S%S    S%S\n"  
       + "S&S     S&S       S&S  S%S    d*S  S&S     S%S SSSS%S\n"  
       + "S&S_Ss  S&S       S&S  S&S   .S*S  S&S     S&S  SSS%S\n"  
       + "S&S~SP  S&S       S&S  S&S_sdSSS   S&S     S&S    S&S\n"  
       + "S&S     S&S       S&S  S&S~YSY%b   S&S     S&S    S&S\n"  
       + "S*b     S*b       d*S  S*S    S%b  S*b     S*S    S&S\n"  
       + "S*S     S*S.     .S*S  S*S    S%S  S*S.    S*S    S*S\n"  
       + "S*S      SSSbs_sdSSS   S*S    S&S   SSSbs  S*S    S*S\n"  
       + "S*S       YSSP~YSSY    S*S    SSS    YSSP  SSS    S*S\n"  
+"SP                     SP                         SP\n"   
+"Y                      Y                          Y    ")




forcaimg = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
vida = 0
palavra = random.choice(dictionary)
acertos = "_" * len(palavra)
lista = []
for letra in acertos:
    lista.append(letra)
   


while vida < 6:
    print("\n"+forcaimg[vida] + "\n")
    for letter in range(len(acertos)):
        print(acertos[letter], end="")
    
    guess = input("\n\n\nInforme uma letra ou tente adivinhar a palavra: ").lower()
    
    if len(guess) == 1:
        i = 0
        for letra in range(len(palavra)):
            if palavra[letra] == guess:
                lista[letra] = guess
                i += 1
    else:
        if guess == palavra:
            print("\nPARABÉNS VOCÊ ACERTOU!!!!")
            input()
            exit()
        else:
            print("\nPalavra incorreta!")
                
    acertos = ''.join(lista)        
    if i == 0:
        vida+=1
    elif acertos == palavra:
            print(f"\nPARABÉNS VOCÊ ACERTOU!!!!\na palavra era {acertos}")
            input()
            exit()
print(f"\n\nACABARAM SUAS CHANCES! VOCÊ PERDEU!!!\nA palavra era: {palavra}")
input()
exit()
    

