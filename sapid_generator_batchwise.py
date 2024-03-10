# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:53:34 2023

@author: JAIN
"""
import numpy as np
import random
import pandas as pd

name=str(input("enter your name :"))
roll_no=str(input("enter your roll number :"))
batch=str(input("Enter your Batch Year:"))

print("")
batch_year=22
batch_year_jr=23

number=np.random.randint(1,50,2)
sapid=random.choice(number)
password='B!tech2022'
password_1="B!tech2023"

if batch=='2022':
    print(f"Your sapid is: 7057{batch_year}000",sapid,sep='')
    print("Your Password is:",password,sep='')
elif batch=='2023':
    print(f"Your sapid is: 7057{batch_year_jr}000",sapid,sep='')
    print("Your Password is:",password_1,sep='')
else:
    print("Sorry We Don't Have this batch year Admissions !!!")
    
