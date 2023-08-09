# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 08:10:27 2023

@author: Juan Carlos
"""

import random

class DispositivoIoT:
    def __init__(self):
        self.__temperatura = 0
        self.__humedad = 0
    
    def get_temperatura(self):
        self.__temperatura = random.randint(20, 30) # Simulamos la lectura de un sensor
        return self.__temperatura
    
    def get_humedad(self):
        self.__humedad = random.randint(40, 60) # Simulamos la lectura de un sensor
        return self.__humedad

# Creación de objeto y llamada a los métodos de acceso a temperatura y humedad
dispositivo = DispositivoIoT()
print(dispositivo.get_temperatura()) # Imprime un valor aleatorio entre 20 y 30
print(dispositivo.get_humedad()) # Imprime un valor aleatorio entre 40 y 60
