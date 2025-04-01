# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 14:08:59 2025

@author: meron
"""

def group_by(func,lst):
    ret = {}
    for i in lst:
        ret[func(i)] = []
    for i in lst:
        ret[func(i)].append(i)
    return ret