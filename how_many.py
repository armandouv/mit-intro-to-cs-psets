# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:28:54 2019

@author: armau
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    i = 0
    x = aDict.values()
    for element in x:
        for m in element:
            i += 1
    return i

