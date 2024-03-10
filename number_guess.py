# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 10:32:14 2023

@author: JAIN
"""

import random
import numpy as np

numbers=np.arange(1,9)

def guess():
    user=int(input("Guess the number between 1-9:  "))

    user_score=0
    result=random.choice(numbers)

    print("the number is",result)

    if result==user:
        print("Yay your luck has shinnedd !!")
        user_score+=1
        print("Your score is",user_score)
    else:
        print("Ahh bad luck :>")
        print("Your score is",user_score)
        
    again=input("do you want to play again? (yes or no) ")
    again=again.lower()
    
    if again=="y":
        guess()
    else:
        print("thank you for playing")
        print(user_score)

guess()

    

    
    