# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 18:52:48 2023

@author: CYBERV
"""

#"D:/CURSOS/EPN/EJERCICIOS/archivos/devices.txt"
# cargar archivo
archivo=open("devices.txt")
for item in archivo:
    print(item)
archivo.close()

#Cargar Archivos y convertir en mayuscula
archivo=open("devices.txt")
for item in archivo:
    item=item.strip() #quitar saltos de lineas
    item=item.upper() #Cambiar todo a mayuscula
    print(item)
archivo.close()

#cargar archivo y guardar en lista
lista=[]
archivo=open("devices1.txt")
for item in archivo:
    item=item.strip() #quitar saltos de lineas
    item=item.upper() #Cambiar todo a mayuscula
    lista.append(item)
    print(item)
archivo.close()



archivo=open("devices1.txt", mode='w')
while True:
    newItem=input("Ingrese informacion paera terminar exit: ")
    if newItem == "exit":
        break          
    archivo.write(newItem + "\n")     
print("All done!")
archivo.close()
   