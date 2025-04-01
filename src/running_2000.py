# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 02:02:23 2025

@author: meron
"""

import time

def running_2000(func,*parameters):
    start_time = time.time()  
    func(*parameters)
    end_time = time.time()  
    execution_time = end_time - start_time
    print(f"Time taken: {execution_time} seconds")
    