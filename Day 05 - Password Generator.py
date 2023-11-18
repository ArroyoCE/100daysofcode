import random

print("Welcome to the password generator!")
letter = int(input("How many letters would like in your password?\n"))
symbol = int(input("How many symbols?\n"))
number = int(input("How many numbers?\n"))
print("")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]



password = []

for _ in range(letter):
    password.append(alphabet[random.randint(0, 24)])

symbols = [
    "!", "#", "$", "&", "%", "+", 
    "*"
    ]

for _ in range(symbol):
    password.append(symbols[random.randint(0, len(symbols)-1)])
    
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for _ in range(number):
    password.append(numbers[random.randint(0, len(numbers)-1)])

password_shuffle = random.sample(password, len(password))


password_join = ''.join(password_shuffle)

print(f"Your password is: {password_join}")
