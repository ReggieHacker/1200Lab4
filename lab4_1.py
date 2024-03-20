#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:37:19 2024

@author: reggiehacker
"""
# ##Example 1
# #import numpy 
# import numpy as np

# #Gravitational constant
# G = float(6.674**(-11))

# #Arrays of masses
# masses = np.array([1.9891*10^30, 5.7219*10^24, 7.34767309*10^22])
# distances = np.array()


# ##Example 2

# #import numpy
# import numpy as np

# #Define known variables
# v0 = 50
# ang = 30
# g = 9.81

# #convert to radians
# angrad =  np.radians(ang)

# #Time intervals
# time_intervals = np.array([0,1,2,3,4,5,6,7,8])

# #Loop
# for i in time_intervals:
#     x = float(v0*np.cos(angrad)*i)
#     y = float((v0*np.sin(angrad)*i)-(0.5*g*(i**2)))
#     print("Your height at ", i, " is ", y, " meters. Your horizontal distance at", i, "is ", x, " meters.") 


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








