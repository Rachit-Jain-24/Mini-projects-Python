# -*- coding: utf-8 -*-
"""
Created on Sat Jul 1 23:15:07 2023
@author: JAIN
"""

import random
import numpy as np
print("Welcome to Rock Paper Scissors Game!!!!!")

rounds=int(input("How many rounds you want to play"))

def rockpaper():
    user = str(input("Choose from rock, paper, scissors: "))
    print("Your choice is", user)
    user_wins=0
    computer_wins=0
    user_wins_1=0
    user_wins_2=0
    user_wins_3=0
    computer_wins_1=0
    computer_wins_2=0
    computer_wins_3=0
    total_win_user=user_wins+user_wins_1+user_wins_2+user_wins_3
    total_win_comp=computer_wins+computer_wins_1+computer_wins_2+computer_wins_3


    possible_choices = ["rock", 'paper', 'scissors']
    computer = random.choice(possible_choices)
    print("Computer's choice is", computer)

    if user == computer:
        print("Both players selected", user, "It's a tie!")

    elif user == "rock":
        if computer == "scissors":
            print("Rock destroys scissors, you win!")
            user_wins_1=user_wins+1
            print("Score of computer:",computer_wins)
        else:
            print("Paper covers rock, you lose!")
            computer_wins_1=computer_wins+1
            print("Score of user:",user_wins_1)
            print("Score of computer:",computer_wins_1)

        print("Score of user :",user_wins_1)
        

    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock, you win!")
            user_wins_2=user_wins_1+1
            print("Score of computer:",computer_wins_1)
        else:
            print("Scissors cut paper, you lose!")
            computer_wins_2=computer_wins_1+1
            print("Score of user:",user_wins_1)
            print("Score of computer:",computer_wins_2)

        print("Score of user :",user_wins_2)
        

    elif user == "scissors":
        if computer == "rock":
            print("Rock destroys scissors, you lose!")
            user_wins_3=user_wins_2+1
            print("Score of computer:",computer_wins_2)
        
        else:
            print("Scissors cut paper, you win!")
            computer_wins_3=computer_wins_2+1
            print("Score of user:",user_wins_2)
            print("Score of computer:",computer_wins_3)

        print("Score of user :",user_wins_3)
        

    
for i in range(rounds):
    print("\nRound ",i+1,"of",rounds,"\n")
    rockpaper()

