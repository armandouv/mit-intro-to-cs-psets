# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:46:57 2019

@author: armau
"""

import math

def polysum(n, s):
    area = (0.25 * n * s**2)/math.tan(math.pi/n)
    per = n * s
    result = area + per**2
    return round(result, 4)

print(polysum(5, 10))