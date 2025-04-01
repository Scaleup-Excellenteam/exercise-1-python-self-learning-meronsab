# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 22:33:59 2025

@author: meron
"""
def cup_of_join(*lists, sep = None):
    """
this func get a few lists end concetanate them ibto one'
 if separetor recive: it will be added between them
    """
    ret = []
    for lst in lists:
        ret.extend(lst)
        if sep != None:
            ret.append(sep)
    return ret
