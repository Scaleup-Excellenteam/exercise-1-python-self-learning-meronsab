# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 12:58:39 2025

@author: meron
"""
from PIL import Image

def remember_remember(image_path):
    img = Image.open(image_path)
    message = []
    w,l = img.size()
    for i in range(w):
        for j in range(l):  
            if img.getpixel((i, j)) == 0:  # בודק אם הפיקסל שחור
                message.append(chr(j))
                break  # עובר לעמודה הבאה

    return "".join(message)



