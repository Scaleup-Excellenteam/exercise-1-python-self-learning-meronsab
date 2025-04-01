# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 22:41:32 2025

@author: meron
"""
def piece_of_cake( prices, optionals=None, **recipe):
    """
    Parameters
    ----------
    prices : dictionary for the price of each item on the recipe
    optionals : list of the items that we can ignore them
    **recipe : dictionary of the items to make the cake with their amount
    -------
this func calculate the minimum cost of the ingrediens for the cake
    """
    if optionals == None:
        optionals = []
    cost = 0
    for item, amount in recipe.items():
        if item not in optionals:
            cost += prices.get(item) * amount / 100 
    return int(cost)
