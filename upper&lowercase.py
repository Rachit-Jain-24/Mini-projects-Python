# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 00:15:22 2023

@author: JAIN
"""

name=input(str("Enter the word: "))

print(name)

namelow=name.lower()
nameup=name.upper()

ask=input(str("Do you want to convert the letters to uppercase or lowercase??"))

ask1='uppercase'
ask2='lowercase'

if ask1:
    print("Uppercased: ",nameup)

    if ask2:
        print("Lowercased: ",namelow)    
