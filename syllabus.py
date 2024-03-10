# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:00:20 2023

@author: JAIN
"""
import PyPDF2
import pandas as pd
import numpy as np

subject=str(input("Enter the subject you want to see syllabus:  "))

if subject=="Dsa" or "dsa":
    print(" 1.Introduction to Dsa\n","2.Linear Data Structure-I\n",
          "3.Linear Data Structure=II\n","4.Non-Linear Data Structure I\n",
          "5.Non-Linear Data Structure-II\n")

if subject=="Dw" or "dw":
    print(" 1.Introduction\n","2.data preprocessing")
    
    

# Prompt the user to enter the file path
file_path = input("Enter the path of the PDF file: ")

# Open the PDF file
with open(file_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
