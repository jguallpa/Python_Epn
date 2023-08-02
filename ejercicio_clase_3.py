# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
@author: Juan Guallpa

"""

#Variables
x=3
x+4
resultados1=x+4
resultado2=x/2


x=3
txt="cisco"
resultado1=x+4
resultado=x//2
opt=txt*x
print("\n"*2)
print("\t"*8)

#forma de unir
str1="cisco"
str2="Networking"
str3="Academy"
space=" "
print(str1+space+str2+space+str3)
print(str1+str2+str3)
print(str1,str2,str3)

x=6
print("El valor de x es:"+x)
#print("El valor de x es:",x) # uso de comentario
print("El valor de x es:"+str(x))

a=int()
b=float()
c=bool()
d=str()
x=6
print("El valor de x es:"+str(x))
print(type(x))


#formatos
pi=22/7
print(pi)
print("{:.2f}".format(pi))
print("{:.6f}".format(pi))


#listas y tuplas

lista=[4,78.9,"R1",True] # dinamica, mutable
tupla=(4,78.9,"R1",True) # estatica, no se puede cambiar

print(lista)
print(tupla)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(tupla[0])

lista[2]="AP1"
#tupla[2]="AP1"

del lista[3]
#del tupla[3]

#dicionario

dict1={"R1":"10.10.10.1",
       4:2,
       "email":"jguallpa@hotmail.com",
       "FONO":"123456"
       }
print(dict1)
print(dict1["R1"])
dict1["NOMBRE"]="JUAN"


#input
nombre=input("Ingrese el nombre: ")
edad=int(input("Ingrese su edad: "))
print(nombre)
print(edad)


