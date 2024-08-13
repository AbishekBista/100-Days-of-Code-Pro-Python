import random
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
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

possible_moves = [rock, paper, scissors]

your_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
if your_move >=3 or your_move < 0:
    print("You made an invalid move")
else:
    print(f"You chose\n{possible_moves[your_move]}")

    computer_move = random.randint(0, 2)
    print(f"\nComputer chose\n{possible_moves[computer_move]}")

    # you chose rock
   
    if your_move == 0:
        if computer_move == 0:
            print("Draw")
        elif computer_move == 1:
            print("You lose")
        else:
            print("You win")
    elif your_move == 1:
        if computer_move == 0:
            print("You win")
        elif computer_move == 1:
            print("Draw")
        else:
            print("You lose")
    elif your_move == 2:
        if computer_move == 0:
            print("You lose")
        elif computer_move == 1:
            print("You win")
        else:
            print("Draw")