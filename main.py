"""
Rock-Paper-Scissor
Scissor
Scissor-Scissor = Draw
Scissor-Rock = Rock win
Scissor-Paper = Paper win

Paper
Paper-Paper = Draw
Paper-Scissor = Scissor win
Paper-Rock = Paper win

Rock
Rock-Rock = Draw
Rock-Scissor = Rock win
Rock-Paper = Paper win

"""
import random
items_list = ["Rock","Paper","Scissor"]
User_choice = input("Enter Your Move = Rock-Paper-Scissor : ").capitalize()
comp_choice = random.choice(items_list)
if User_choice in items_list:
    print(f"User_choice = {User_choice}  comp_choice = {comp_choice}")
    if User_choice == comp_choice:
        print("Draw")
    elif User_choice == 'Scissor':
        if comp_choice == 'Rock':
            print("Comp Win")
        else:
            print("User Win")
    elif User_choice == 'Paper':
        if comp_choice == "Scissor":
            print("Comp Wins")
        else:
            print("User Wins")
    elif User_choice == "Rock":
        if comp_choice == "Scissor":
            print("User Wins")
        else:
            print("Comp Wins")
else:
    print("Invalid OutPut")