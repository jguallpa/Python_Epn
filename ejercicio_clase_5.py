# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 18:38:03 2023

@author: Juan Guallpa
"""

#funciones

def resta(a,b):
    print (a-b)
    print("\n"*2)

resta(5,2)
resta(2,5)
resta(a=5,b=2)
resta(a=2,b=5)
resta(5,b=2)


#multiplicar

def multiply(a=5,b=3):
    print(a*b)
    
resultado=multiply()
print(resultado)
opt=resultado+1
print(opt)


# retornar valores
def multiply(a=5,b=3):
    print("el resultadode multiplicar",a,"*",b, " es: ",a*b)
    return(a*b) # retorna el valor de calculo

resultado=multiply()    
#resultado=multiply(10,5)
print(resultado)
print(type(resultado))
opt=resultado+1
print(opt)


#funcion lista como argumento
def funlista(lista):
    for item in lista:
        print("Hola",item)
        print("")
        
funlista(["Juan"])
funlista(["juan","Carlos"])
funlista(["luis","Carlos","Alejandro"])



def crealista(n):
    lista=[]
    for item in range(n):
        lista.append(item)
    return lista

print(crealista(10))


#funcion anonima lambda

#modulo paquetes y funciones
#https://docs.python.org/3/library/index.html

#metodo 1
import math
import sys

pi=22/7

def sin():
    return 9.99999

print(sin())
print(pi)

opt=math.sin(math.pi/2)
print(opt)

#metodo 2

from math import sin,pi

opt=sin(pi/2)
print(opt)

#metodo 3 agresivo carga toda las caracteristicas

from math import *
opt=sin(pi/2)
print(opt)




