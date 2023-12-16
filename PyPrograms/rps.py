# Rock Paper Scissors
import random
import time

def rock_paper_scissors():
  # Options for the game
  options = ["rock", "paper", "scissors"]

  print("\033[034mWelcome to Rock Paper Scissors!\033[0m")

  while True:
    print("")
    user_choice = input("rock, paper, scissors?: ").lower()

    if user_choice not in options:
        print("\033[31mInvalid choice.\033[0m")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("\033[33mTie.\033[0m")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("\033[32mYou won.\033[0m")
    else:
        print("\033[31mYou lost.\033[0m")

print("""____________________  _________
\______   \______   \/   _____/
 |       _/|     ___/\_____  \ 
 |    |   \|    |    /        \                                         
 |____|_  /|____|   /_______  /
       \/                  \/ """)
print("")

rock_paper_scissors()