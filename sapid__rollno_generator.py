# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:53:34 2023

@author: JAIN
"""
import numpy as np
import random

name=str(input("enter your name :"))
#roll_no=str(input("enter your roll number :"))
batch=str(input("Enter your Batch Year:"))

print("")
batch_year=22
batch_year_jr=23

#roll_number=np.random.randint(10,50,2)


number=np.random.randint(1,50,2)
sapid=random.choice(number)
rollno=sapid+2

if batch=='2022':
    print(f"Your sapid is: 7057{batch_year}000",sapid,sep='')
elif batch=='2023':
    print(f"Your sapid is: 7057{batch_year_jr}000",sapid,sep='')

print("Your Roll Number is : L0",rollno,sep="")