# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 23:15:07 2023

@author: JAIN
"""

import random

rounds=int(input("how many rounds do you want to play--"))

user=str(input("Choose from rock , paper , scissors:"))
print("your choice is ",user)

possible_choices=["rock",'paper','scissors']
computer=random.choice(possible_choices)

print("computer's choice is ",computer)


if user==computer:
    print("Both players selected" ,user,"It's a tie!")
elif user=="rock":
    if computer=="scissors":
        print("Rock destroys scissors , you win!")
    else:
        print("paper covers rock , you lose!")
elif user=="paper":
    if computer=="rock":
        print("Paper covers rock ,you win !")
    else:
        print("scissors cuts paper, you win!")

elif user=="scissors":
    if computer=="rock":
        print("rock destroys scissors , you win!")
    else:
        print("scissor cuts the paper")
    







