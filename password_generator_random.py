# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:48:31 2023

@author: JAIN
"""

import random

length=int(input("enter the length of your password :"))

usname=input("username :")

username=""

characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"

password=""

for i in range(length):
    username+=random.choice(characters)
    
for i in range(length):
    password+=random.choice(characters)

 
print("password :",password)

print("")

print("your username is ",username)
print("your password is ",password)

