# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""
import numpy as np

weight = float(input())
height = float(input())
BMI = np.round(weight/height**2, 3)
print(BMI)
