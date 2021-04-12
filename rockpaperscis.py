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

player_input = input("Enter your input 0 for Rock, 1 for Paper Or 2 for Scissors")
if player_input == "0":
    print(rock)
elif player_input == "1":
    print(paper)
else:
    print(scissors)  

computer_choice = [rock,paper,scissors]
ai_player = random.choice(computer_choice)

print("the computer choice is ", ai_player)

if ai_player == rock and player_input == "2":
    print("Computer as won")
elif ai_player  == paper and player_input == "0":
    print("Computer as won")    
elif ai_player == scissors and player_input == "1":
    print("Computer as won")
elif ai_player == rock and player_input == "0":
    print("It is a draw")
elif ai_player == paper and player_input == "1":
    print("It is a draw")    
elif ai_player == scissors and player_input == "2":
    print("It is a draw")
else:
  print("The player as won")       

