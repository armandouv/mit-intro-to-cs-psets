# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 23:00:23 2019

@author: armau
"""

"""
balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

Prints out the remaining balance
"""
def credit(annualInterestRate, balance):
    mont_int = annualInterestRate/12
    for i in range (12):
        balance -= balance*mont_int
        newbalance = balance + balance * mont_int
        balance = newbalance
        
    print("Remaining balance:", round(newbalance, 2))
    
def credit1(annualInterestRate, balance, pay):
    mont_int = annualInterestRate/12
    for i in range (12):
        newbalance = balance + balance * mont_int
        newbalance -= pay
        balance = newbalance
        return balance
        
    print("Remaining balance:", round(balance, 2))