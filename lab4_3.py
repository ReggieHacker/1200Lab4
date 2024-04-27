#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:48:14 2024

@author: reggiehacker
"""

##Example 3

#import
import numpy as np

#resistor arrays
resistor_series = np.array([100, 200, 250])
resistor_parallel = np.array([150, 250, 300])

#calculate total series resistance
total_series = np.sum(resistor_series)

#define list
inv_parallel=[]

#loop for parallel sequence
for r in resistor_parallel:
    x = 1/r
    inv_parallel.append(x)
    
total_parallel = (np.sum(inv_parallel))**-1

print('The total resistance of the series circuit is', total_series, 'Ohms')
print('The total resistance of the parallel circuit is', total_parallel, 'Ohms')
