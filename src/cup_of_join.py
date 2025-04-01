# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 22:33:59 2025

@author: meron
"""

def cup_of_join(*lists, sep = "-"):
    ret = []
    for lst in lists:
        ret.extend(lst)
        ret.append(sep)
    ret.pop()
    return ret
#print(join([1,2],[5],[1,3,6],sep = '|'))