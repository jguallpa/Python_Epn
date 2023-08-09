# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 08:01:22 2023

@author: Juan Carlos
"""

class Vehiculo:
    def __init__(self, velocidad, posicion, direccion):
        self.velocidad = velocidad
        self.posicion = posicion
        self.direccion = direccion
    
    def mover(self):
        # Implementación genérica para mover un vehículo
        print("El vehiculo se mueve")

class Coche(Vehiculo):
    def __init__(self, velocidad, posicion, direccion, num_ruedas):
        super().__init__(velocidad, posicion, direccion)
        self.num_ruedas = num_ruedas
    
    def conducir(self):
        # Implementación específica para conducir un coche
        print("El auto inicío la conducción")

class Moto(Vehiculo):
    def __init__(self, velocidad, posicion, direccion, forma_control):
        super().__init__(velocidad, posicion, direccion)
        self.forma_control = forma_control
    
    def acelerar(self):
        # Implementación específica para acelerar una moto
        print("La moto acelera")
mi_coche = Coche(velocidad=100, posicion=(0, 0), direccion='este', num_ruedas=4)
mi_moto = Moto(velocidad=80, posicion=(10, 10), direccion='sur', forma_control='manubrio')

print(mi_coche.velocidad)  # Output: 100
print(mi_moto.posicion)  # Output: (10, 10)

mi_coche.conducir()  # Output: Implementación específica para conducir un coche
mi_moto.acelerar()  # Output: Implementación específica para acelerar una moto

