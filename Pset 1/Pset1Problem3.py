# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:27:39 2019

@author: armau
"""

word = input("Type your word\n")
cand = a = news = ""

for i in word + " ":
    if cand <= i:
        a += i
    else:
        if len(a) > len(news):
            news = a
        a = i
    cand = i

print("Longest substring in alphabetical order is:", news)