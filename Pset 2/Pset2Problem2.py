# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:03:34 2019

@author: armau
"""
"""
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

annualInterestRate = float(input("Annual interest: "))
balance = int(input("Balance: "))

monthInt = annualInterestRate/12
fixed = 0

while (True):
    update = 0
    unpaid = balance
    
    fixed += 10
    
    for i in range (12):
        unpaid -= fixed
        update = unpaid + (monthInt * unpaid)
        unpaid = update
        print(update)
        
    if unpaid <= 0:
        break

print("Lowest Payment:", fixed)