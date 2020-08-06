# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:28:32 2019

@author: armau
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
        
    if len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    
    mid = aStr[len(aStr)//2]
    midind = len(aStr)//2
    leng = len(aStr)
    
    if mid == char:
        return True
    else:
        if char < mid:
            return isIn(char, aStr[:midind])
        else:
            return isIn(char, aStr[(midind + 1):(leng + 1)])