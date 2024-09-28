# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. 
For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""
print('Input 4-digit number pls')
str = input()

try:
    digits = [int(i) for i in str]
    print(f"{' + '.join(str)} = {sum(digits)}")
except:
    print('smth is wrong with the input')

