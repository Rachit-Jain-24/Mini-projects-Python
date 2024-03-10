# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:42:20 2023

@author: JAIN
"""

import random
import matplotlib.pyplot as plt

rounds = int(input("How many rounds do you want to play? "))
user_wins = 0
computer_wins = 0

user_choices = []
computer_choices = []

for _ in range(rounds):
    user = input("Choose from rock, paper, scissors: ")
    print("Your choice is", user)

    possible_choices = ["rock", "paper", "scissors"]
    computer = random.choice(possible_choices)
    print("Computer's choice is", computer)

    user_choices.append(user)
    computer_choices.append(computer)

    if user == computer:
        print("Both players selected", user, "It's a tie!")
    elif user == "rock":
        if computer == "scissors":
            print("Rock destroys scissors, you win!")
            user_wins += 1
        else:
            print("Paper covers rock, you lose!")
            computer_wins += 1
    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock, you win!")
            user_wins += 1
        else:
            print("Scissors cuts paper, you lose!")
            computer_wins += 1
    elif user == "scissors":
        if computer == "rock":
            print("Rock destroys scissors, you lose!")
            computer_wins += 1
        else:
            print("Scissors cuts paper, you win!")
            user_wins += 1

print("Analysis:")
print("Human wins:", user_wins)
print("Computer wins:", computer_wins)

# Data analysis graphs
choices = ["rock", "paper", "scissors"]
user_choice_counts = [user_choices.count(choice) for choice in choices]
computer_choice_counts = [computer_choices.count(choice) for choice in choices]

plt.bar(choices, user_choice_counts, label="Human")
plt.bar(choices, computer_choice_counts, label="Computer")
plt.xlabel("Choices")
plt.ylabel("Counts")
plt.title("Choice Counts")
plt.legend()
plt.show()
