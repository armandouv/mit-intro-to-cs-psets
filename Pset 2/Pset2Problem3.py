# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:43:00 2019

@author: armau
"""

annualInterestRate = float(input("Annual interest: "))
balance = int(input("Balance: "))

monthInt = annualInterestRate/12
lower = balance / 12
upper = balance * (1 + monthInt)**12 / 12

while (True):
    test = (upper + lower) / 2
    update = 0
    unpaid = balance

    for i in range (12):
        unpaid -= test
        update = unpaid + (monthInt * unpaid)
        unpaid = update
        print(update)
    
    if -1 < unpaid < 1:
        break
    elif unpaid >= 1:
        lower = test
    else:
        upper = test

print("Lowest Payment:", test)