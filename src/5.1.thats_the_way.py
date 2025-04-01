# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 22:04:46 2025

@author: meron
"""
import os
def thats_the_way(directory):
    """
    this function gets a path to directory and return all the files that start with "deep"
    in that directory
    """
    files = os.listdir(directory)
    deep_files = [file for file in files if file.startswith("deep")]
    return deep_files
