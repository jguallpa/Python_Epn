# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:41:38 2023

@author: CYBERV
"""

# alias para modulos o librerias 

#Normal
import math
print(math.sin(math.pi/2))

# con alias
import math as m
print(m.sin(m.pi/2))



from math import sin as s, pi as p 
opt=s(p/2)
print (opt)
