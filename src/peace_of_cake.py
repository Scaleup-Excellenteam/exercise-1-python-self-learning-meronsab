# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 22:41:32 2025

@author: meron
"""
def get_recipe_price(pricedict, optionals=[], **recipe):
    cost = 0
    for item, amount in recipe.items():
        if item not in optionals:
            cost += pricedict.get(item) * amount / 100 

    return int(cost) 
print(get_recipe_price({}))
print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
