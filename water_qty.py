# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:20:33 2023

@author: JAIN
"""

print("Hi how much water have you filled today=  ")
water_qty=float(input())

print("your total water qty is ",water_qty)

print("Dividing water qty into 4 needs 1.Bathing 2.Cooking 3.Cleaning 4.Drinking")

bathing=int(input("Enter the qty for bathing you need: "))
cooking=int(input("Enter the qty for cooking you need: "))
cleaning=int(input("Enter the qty for cooking you need: "))
drinking=int(input("Enter the qty for cooking you need: "))

sum_water=bathing+cooking+cleaning+drinking

print("The amt of water you demanded today is ",sum_water,"ltrs","out of",water_qty,"ltrs")


