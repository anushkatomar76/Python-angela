print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm ?"))
bill = 0

if height > 120:
    print("you can ride the rollercoaster")
    age = int(input("What is your age?"))

    if age <= 12:
        bill = 5
        print("childs tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youths ticets are $7")
    else:
        bill = 12
        print("Adults tickets are $12")
    wants_photo = input("Do you want to have a photo take? Type y for yes and n for no.")
    if wants_photo == "y":
        bill = bill + 3

    print(f"Your bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")