from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
if num == 1:
    computer_move = "rock"
elif num == 2:
    computer_move = "paper"
elif num == 3:
    computer_move = "scissors"

# Ask a user to enter their move
print("*" * 19)
print("Rock Paper Scissors")
print("*" * 19)
player_move = input("\nWhat's your move?").lower()

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
if player_move == "rock":
    print(rock)
elif player_move == "paper":
    print(paper)
elif player_move == "scissors":
    print(scissors)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print("\nComputer's move:")
if computer_move == "rock":
    print(rock)
elif computer_move == "paper":
    print(paper)
else:
    print(scissors)

# Figure out who wins and print the result!
if computer_move == player_move:
    print("IT'S A TIE!")
elif computer_move == "rock" and player_move == "paper":
    print("YOU WIN!")
elif computer_move == "paper" and player_move == "scissors":
    print("YOU WIN!")
elif computer_move == "scissors" and player_move == "rock":
    print("YOU WIN!")    
else:
    print("YOU LOSE!")