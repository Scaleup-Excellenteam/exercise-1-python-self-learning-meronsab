# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 01:37:06 2025

@author: meron
"""
def interleave(*itera):
    """
this function gets number of lists and merge them into one long list by keeping the order
    """
    ret = []
    bigest = 0
    for ite in itera:
        bigest = max(bigest, len(ite))
    for i in range(bigest):
        for ite in itera:
            if i < len(ite):
                ret.append(ite[i])
    return ret
def generator_interleave(*itera):
    """
    this function does the same but using yield to return them one by one
    """
    bigest = 0
    for ite in itera:
        bigest = max(bigest, len(ite))
    for i in range(bigest):
        for ite in itera:
            if i < len(ite):
                yield (ite[i])