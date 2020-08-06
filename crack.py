# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:29:05 2019

@author: armau
"""

from sys import *
from string import *
from itertools import permutations

letters = " " + ascii_letters
salts = ascii_letters + digits

def genWord():
	for i in range(len(combinations(letters, 5))): yield tuple(combinations(letters, 5)[i])

def genSalt():
	yield from combinations(salts, 2)

def convert(tup):
	st = ''.join(tuple(tup))
	return st.strip()

def jaja(c):
    while True:
        x = combinations(c, 2)
        for i in x:
            yield i
c = "cdc"

print(jaja(c))