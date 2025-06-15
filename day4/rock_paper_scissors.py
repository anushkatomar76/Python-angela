#rock paper scissors
import random


rock = '''
     _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

games_image = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(games_image[user_choice])

computer_choice = random.randint(0,2)
if user_choice >= 0 and user_choice <= 2:
    print(f"computer chose: \n {games_image[computer_choice]}")


if user_choice >= 3  or user_choice < 0:
    print("typed an invalid output. you lose!")

elif user_choice == 0 and computer_choice == 2:
    print("you win!")

elif user_choice == 2 and computer_choice == 0:
    print("you lose!")

elif user_choice == 1 and computer_choice == 0:
    print("you win!")

elif computer_choice > user_choice :
    print("You lose!")

elif computer_choice == user_choice:
    print("its a draw")









