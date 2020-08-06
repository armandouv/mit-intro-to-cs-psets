# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:55:07 2019

@author: armau
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggest = 0
    keys = []
    if not aDict:
        return None
    else:
        for element in aDict.items():
            i = 0
            for x in element[1]:
                i += 1
            if i > biggest:
                biggest = i
                keys.clear()
                keys.append(element[0])
            elif i == biggest:
                keys.append(element[0])
        return keys