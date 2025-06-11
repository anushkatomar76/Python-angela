print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm ?"))

if height > 120:
    print("you can ride the rollercoaster")
    age = int(input("What is your age?"))

    if age <= 12:
        print("you will pay $5")
    elif age <= 18:
        print("you will pay $7")
    else:
        print("ypu will pay $7")
else:
    print("Sorry, you have to grow taller before you can ride.")