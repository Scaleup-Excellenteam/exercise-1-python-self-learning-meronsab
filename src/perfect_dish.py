# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 01:01:33 2025

@author: meron
"""

def find_perfect_dish(upper_bound=10000):
    for dish in range(6, upper_bound):
        dividers = [1]
        for num in range(2,dish//2 + 1):
            if dish % num==0:
                dividers.append(num)
            if num == dish//2:
                if sum(dividers) == dish:
                    yield dividers


for dish in find_perfect_dish():
    print(dish,sum(dish))
    