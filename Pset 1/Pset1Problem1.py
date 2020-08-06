# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:18:57 2019

@author: armau
"""
word = input("Type your word\n")
vowels = 0

for i in range(len(word)):
    if word[i] in "aeiou":
        vowels += 1

print("Number of vowels:", vowels)