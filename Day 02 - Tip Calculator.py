print("Welcome to the tip calculator.")
total = float(input("What was the total bill?\n"))
people = int(input("How many people to split the bill?\n"))
tip = int(input("what percentage tip would you like to give? 10, 12 or 15?\n"))
print(f"Each person should pay: $", round(((total/people)*(1+tip/100)), 2), sep="")
 

