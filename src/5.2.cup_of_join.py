# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 22:33:59 2025

@author: meron
"""

def cup_of_join(*lists, sep = 1):
    ret = []
    for lst in lists:
        ret.extend(lst)
        if sep != 1:
            ret.append(sep)
   
    return ret
