# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 22:15:13 2025

@author: meron
"""
import random
from datetime import datetime, timedelta
def vinigrate(d1,d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    if d1 > d2:
        d1, d2 = d2, d1  
    delta_days = (d2 - d1).days
    random_days = random.randint(0, delta_days)
    random_date = d1 + timedelta(days=random_days)
    day_of_week = random_date.strftime("%A")
    if str(day_of_week)!="Monday":
        print("i dont have vinigrate")
    return random_date

# דוגמה לשימוש
D1 = "2023-01-01"
D2 = "2023-12-31"
print(vinigrate(D1, D2))
