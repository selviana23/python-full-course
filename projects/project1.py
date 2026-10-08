import random

choices = ["rock", "paper", "scissors"]

player = input("Choose rock, paper, or scissors: ")

computer = random.choice(choices)

print("You choose:", player)
print("Computer choose:", computer)

if player == computer:
    print("It's a draw!")

elif (
    (player == "rock" and computer == "scissors")
    or
    (player == "paper" and computer == "rock")
    or
    (player == "scissors" and computer == "paper")
):
    print("You win!")

else:
    print("Computer wins!")