# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 01:37:06 2025

@author: meron
"""

def communicating_vessels(*itera):
    ret = []
    bigest = 0
    for ite in itera:
        if len(ite)>bigest:
            bigest = len(ite)
    for i in range(bigest):
        for ite in itera:
            if i < len(ite):
                ret.append(ite[i])
    return ret

#print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
#['a', 1, '!', 'b', 2, '@', 'c', 3, '#']       