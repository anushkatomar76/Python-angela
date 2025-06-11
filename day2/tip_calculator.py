print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $ "))

tip = float(input("How much tip would you like to give ? 10, 12, or 15? "))

split = float(input("How many people to split the bill? "))

tips = (tip/100) * bill

final = (bill + tips) / split
input(f"Each person should pay: $ {round(final,2)}")
