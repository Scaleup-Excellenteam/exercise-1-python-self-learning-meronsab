# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 02:02:23 2025

@author: meron
"""

import time
def running_2000(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()  
    execution_time = end_time - start_time
    return execution_time