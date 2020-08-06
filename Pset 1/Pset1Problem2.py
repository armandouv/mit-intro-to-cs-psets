# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:17:11 2019

@author: armau
"""

word = input("Type your word\n")
times = 0

for i in range(0, len(word) - 2):
    if word[i:i+3] in "bob":
        times += 1

print("Number of times bob occurs:", times)