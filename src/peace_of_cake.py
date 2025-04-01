# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 22:41:32 2025

@author: meron
"""
def piece_of_cake(pricedict, optionals=[], **recipe):
    cost = 0
    for item, amount in recipe.items():
        if item not in optionals:
            cost += pricedict.get(item) * amount / 100 

    return int(cost) 
