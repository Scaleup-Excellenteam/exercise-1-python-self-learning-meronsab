# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 22:04:46 2025

@author: meron
"""
import os
def find_deep_files(directory):
    files = os.listdir(directory)
    deep_files = [file for file in files if file.startswith("deep")]
    return deep_files
def check_image():
    deepnum = len(find_deep_files("image"))
    if deepnum==2:
        print("success! the directory image contains excactly 2 files that start with /'deep/'")
    else:
        print("wrong! the directory image contains ",deepnum," files that start with /'deep/'")
        