# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:34:17 2019

@author: armau
"""

def genPrimes():
    primes = [2]
    yield 2
    
    primes.append(3)
    yield 3
    
    
    def isPrime():
        for num in primes:
            if cand % num == 0:
                #cand += 1
                return False
        return True
    
    cand = 5
    while True:
        while not isPrime():
            cand += 2
        primes.append(cand)
        yield cand
        cand += 2
    
    
            
    