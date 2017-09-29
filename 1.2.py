#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 23:47:03 2017

@author: apple
"""

import matplotlib.pyplot as plt
x = 0
v = 40
dt = 0.01
x = [1] * 40
for i in range (0,39):
    x[i+1]=x[i]+v*dt
t = [0] * 40
for i in range (0,39):
    t[i+1] = t[i] + dt
plt.plot(t, x,'b-.')
plt.xlabel("t") 
plt.ylabel("x")
plt.title('x-t relation') 
plt.show()
