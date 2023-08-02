# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 18:38:23 2023

@author: Juan Guallpa
"""

#if simple doble condicional
datos=100
nativa=1

if datos==nativa:
    print("Las VLAN son iguales")
else: 
    print("Las VLAN son diferentes")
    
    
#if elif    
acl=int(input("Ingrese el # de ACL: "))

if acl>=1 and acl<=99:
    print("Es una ACL standar")
elif acl >=100 and acl<=199:
    print("es una ACL Extendida")
else:
    print ("El # Ingresado no es una ACL")
    


#ejercicio

space = " "
nombre=input("Ingrese Nombre: ")
apellido=input("Ingrese Apellido: ")
ciudad=input("Ingrese Ciudad: ")
edad=int(input("Ingrese la edad:"))

print (nombre + space + apellido + space + ciudad + space + str(edad)) 

if edad>= 1 and edad<= 12:
    print ("Es niño")
elif edad >12 and edad<=18:
    print ("Es adolecente")
elif edad >18 and edad<=60:
   print ("es adulto")
elif edad>60 :
   print ("es tercera edad")
else:
    print("super hombre")
    
    
#for

lista=[14324,24234,1342343,234234,54565,567635,234234]
for item in lista:
    print(item)
    
    
for i in range(1,10+1,1):
    print(i,end=" * ")
    

lista["R1","R2","R3",
      "S1","S2","S3",
      "AP1","AP2","AP3"]

for elemento in lista:
    if "R" in elemento:
        print (elemento)

# ejercicio

#listas de asignacion
listar_r=[]
listar_s=[]
listar_a=[]
listar_v=[]

#lista principal
lista=["R1","R2","R3",
      "S1","S2","S3",
      "AP1","AP2","AP3",
      "FW2","PC1","PC2"]

for elemento in lista:
    if "R" in elemento:
        listar_r.append(elemento)
        print (listar_r)
    elif "S" in elemento:
        listar_s.append(elemento)
        print(listar_s)
    elif "AP" in elemento:
        listar_a.append(elemento)
        print(listar_a)
    else:
        listar_v.append(elemento)
        print(listar_v)
        

# while

contar=input("Ingrese el numero al que debo contar: ")
contar=int(contar)
contador=1
while contador <=contar:
    print(contador)
    contador+=1



contar=input("Ingrese el numero al que debo contar: ")
contar=int(contar)
contador=1
while True:
    print(contador)
    contador+=1
    if contador>contar:
        break #termina
    

#ejercicio
while True:
    x=input("Eneter a number to count to: ")
    if x=='q' or x== 'quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
    

#funciones
#def define una funcion
def mensaje ():
    print("Ingrese un dato: ")

    
mensaje()
a=input()
mensaje()
b=input()
mensaje()
c=input()

print(a+b+c)

"""
4 fuentes 
de python
de modulos
de codigo---propios
las funciones inicializar, ser unicas
"""   

def saludo(nombre):
    print("hola",nombre,"\n")
    
saludo("juan")
        
#**********

def saludo2(nombre="CEC",apellido="EPN"):
    print("hola",nombre, apellido)
    
saludo2("Juan","Guallpa")
    
#************

def direccion(ciudad, barrio,calle):
    print("La direccion de entrega es:")
    print("la ciudad:", ciudad)
    print("Barrio es:",barrio)
    print("calle",calle)
    
ci=input("Ingrse ciudad:")
ba=input("ingrese barrio:")
ca=input("Ingrese calle:")

direccion(ci,ba,ca)




