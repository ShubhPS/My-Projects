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

# Write your code below this line 👇
options = [rock, paper, scissors]
player_choice = int(input("Choose : 0 for Rock, 1 for Paper, 2 for Scissors"))
print(options[player_choice])
AI_choice = random.randint(0, 2)
print(f"Computer chooses : {options[AI_choice]}")

if AI_choice == player_choice:
    print("Draw")
elif player_choice == AI_choice - 1:
    print("You lose")
elif player_choice == AI_choice + 1:
    print("You win")
elif player_choice == 2 and AI_choice == 0:
    print("You lose")
elif player_choice == 0 and AI_choice == 2:
    print("You win")
else:
    print("wrong")
