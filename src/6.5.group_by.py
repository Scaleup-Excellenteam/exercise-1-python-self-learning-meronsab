# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 14:08:59 2025

@author: meron
"""
def group_by(func,lst):
    """
this func crate a dictionary with the value that func return as key 
and all the arguments that give that value as val to that key
    """
    ret = {}
    for i in lst:
        ret[func(i)] = []
    for i in lst:
        ret[func(i)].append(i)
    return ret
