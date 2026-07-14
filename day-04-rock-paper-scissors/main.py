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

import random
game_images = [rock, paper, scissors]

game_choice_1 = input("Insert your choice: 0 for Rock, 1 for Paper, 2 for Scissors: ")
game_choice = int(game_choice_1)
second_choice = random.randint(0, 2)

print(game_images[game_choice])
print(game_images[second_choice])

if game_choice == second_choice:
    print("Draw")
elif game_choice == 0:
    if second_choice == 1:
        print("You loose!")
    else:
        print("You win!")

elif game_choice == 1:
    if second_choice == 0:
        print("You win!")
    else:
        print("You lose!")
elif game_choice == 2:
    if second_choice == 0:
        print("You loose!")
    else:
        print("You win!")

