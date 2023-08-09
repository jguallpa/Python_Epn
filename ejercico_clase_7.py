# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 18:55:33 2023

@author: CYBERV
"""
# Validar4 errores

print("inicio")
try:
    print("1")
    x=1/0
    print("2")
except:
    print("Hay un error")
print("3")
print("fin")

#prueba try

try:
    x =int (input("Enter a number:"))
    y = 1/x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")
print("THE END.")


# prueba try
try:
    y = 2 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")
except:
    print("Error")

print("THE END.")


