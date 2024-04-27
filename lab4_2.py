#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:48:14 2024

@author: reggiehacker
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:37:19 2024

@author: reggiehacker
"""

##Example 2

#import numpy
import numpy as np

#Define known variables
v0 = 50
ang = 30
g = 9.81

#convert to radians
angrad =  np.radians(ang)

#Time intervals
time_intervals = np.array([0,1,2,3,4,5,6,7,8])

#Loop
for i in time_intervals:
    x = float(v0*np.cos(angrad)*i)
    y = float((v0*np.sin(angrad)*i)-(0.5*g*(i**2)))
    print("Your height at ", i, " is ", y, " meters. Your horizontal distance at", i, "is ", x, " meters.") 
