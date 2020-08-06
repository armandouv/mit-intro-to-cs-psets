# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:44:28 2019

@author: armau
"""
from itertools import product
from string import *

letters = " " + ascii_letters
salts = ascii_letters + digits

def convert(tup):
	st = ''.join(tuple(tup))
	return st.strip()

salts = [convert(x) for x in product(salts, repeat=2)]

for wordT in product(letters, repeat=5):
	print(convert(wordT))