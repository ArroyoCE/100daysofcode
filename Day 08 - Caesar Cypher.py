print("""  $$$$$$\                                                    
$$  __$$\                                                   
$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$\   $$$$$$\  
$$ |       \____$$\ $$  __$$\ $$  _____| \____$$\ $$  __$$\ 
$$ |       $$$$$$$ |$$$$$$$$ |\$$$$$$\   $$$$$$$ |$$ |  \__|
$$ |  $$\ $$  __$$ |$$   ____| \____$$\ $$  __$$ |$$ |      
\$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$$$$$$  |\$$$$$$$ |$$ |      
 \______/  \_______| \_______|\_______/  \_______|\__|      
                                                            
                                                            
                                                            
 $$$$$$\                      $$\                           
$$  __$$\                     $$ |                          
$$ /  \__|$$\   $$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$ |      $$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ |      $$ |  $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$\ $$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$  |\$$$$$$$ |$$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |      
 \______/  \____$$ |$$  ____/ \__|  \__| \_______|\__|      
          $$\   $$ |$$ |                                    
          \$$$$$$  |$$ |                                    
           \______/ \__|                       


""")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
positions = []
work = input("\n\nType 'encode' to encrypt, and 'decode' to decrypt:\n")
while True:
    try:
        shift = int(input("What's the shift number?\n"))
    except TypeError:
        print("Use integers.")
    else:
        break
while True:
    if work.lower() == "encode":
        message = input("Type your message:\n")

        for letter in message.lower():
            for position in range(36):
                if letter == alphabet[position]:

                    positions.append(position)
                    break
                elif letter == " ":
                    positions.append(-1)
                    break

        for position in range(len(positions)):
            if positions[position] != -1 and positions[position] + shift > 35:
                positions[position] = (positions[position]+shift)-35
            elif positions[position] != -1:
                positions[position] = positions[position]+shift

        encoded = ""
        for position in positions:
            if position == -1:
                encoded += " "
            else:
                encoded += alphabet[position]
        print(f"\nYour Encoded Message is {encoded}.")
    elif work.lower() == "decode":
        message = input("Type the message you would like to decode:\n")

        for letter in message.lower():
            for position in range(36):
                if letter == alphabet[position]:
                    positions.append(position)
                    break
                elif letter == " ":
                    positions.append(-1)
                    break

        for position in range(len(positions)):
            if positions[position] != -1 and positions[position] - shift < 0:
                positions[position] = (positions[position] - shift) + 35
            elif positions[position] != -1:
                positions[position] = positions[position] - shift

        encoded = ""
        for position in positions:
            if position == -1:
                encoded += " "
            else:
                encoded += alphabet[position]
        print(f"\nYour Decoded Message is {encoded}.")

    break


input()
