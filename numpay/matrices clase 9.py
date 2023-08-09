# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 20:42:04 2023

@author: CYBERV
"""

import numpy as np

unos=np.ones((3,4))
print(unos)
ceros=np.zeros((3,4))
print(ceros)

aleatorios=np.random.random((2,2))
print(aleatorios)

mt1=np.full((6,6), 100)
print(mt1)

mt3=np.arange(0,30,5)
print(mt3)

a=np.array([(1,2,3,4),(3,4,5,6)])
print(a)
print("\n"*1)
print(a[1,1])

x=np.array([(1,2,3,4),(3,4,5,6)])
y=np.array([(1,2,3,4),(3,4,5,6)])
print(x+y)
print("\n")
print(x-y)
print("\n")
print(x*y)
print("\n")
print(x/y)