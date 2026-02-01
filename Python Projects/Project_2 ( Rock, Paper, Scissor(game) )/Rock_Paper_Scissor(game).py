# Rock, paper, scissor game :

#  WORKFLOW OF PROJECT:
#  1- Input from user(Rock, paper, scissor)
#  2- Computer choice (Computer will choose randomly not conditionally)
#  3- Result print

#  Cases:
#  A- Rock
#  Rock - Rock = tie
#  Rock - Paper = Paper win
#  Rock - scissor = Rock win

#  B- Paper
#  Paper - Paper = tie
#  Paper - Rock = Paper win
#  Paper - Scissor = Scissor win

#  C- Scissor
#  Scissor - Scissor = tie
#  Scissor - Rock = Rock win
#  Scissor - Paper = Scissor win

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor= ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same:  Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers the Rock - Computer Win")
    else:
        print("Rock smashes the Scissor - You win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts the paper - Computer Win")
    else:
        print("Paper covers the Rock - You win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts the paper - You win")
    else:
        print("Rock smashes the Scissor - Computer win")

print("Thank you for playing the game...")