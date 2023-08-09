# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 18:49:36 2023

@author: CYBERV
"""

class MiPrimeraClase:
    pass


objeto1=MiPrimeraClase()
objeto2=MiPrimeraClase()


class MiSegundaClase:
    pass


Objeto3=MiSegundaClase()
Objeto4=MiSegundaClase()


#ejercicio

class Robot:
    def __init__(self, marca, procedencia, color, modelo):
        self.marca= marca
        self.procedencia = procedencia
        self.color = color
        self.modelo = modelo
        
    def ordenes(self):
        print("Recibe ordenes por voz")
        
    def rutinario(self):
        print("Haces las mismas cosas siempre")

    def camina(self):
        print("El robot camina como un humano")

    def procesa(self):
        print("Procesa la ordenes enviadas para actuar")

    def imparable(self):
        print("El robot no se cansa")        
        



class Macscota:
    def __init__(self, color, sexo, edad, vacuna):
        self.color = color
        self.sexo = sexo
        self.edad =edad
        self.vacuna = vacuna
        
    def animal(self):
        print("La Mascota es un animal domesticado")
    
    def juega(self):
        print("La Mascota es jugetona")
        
    def comer(self):
        print("La mascota come solo carne")
        
    def corre(self):
        print("La mascota le gusta correr en el campo")
        
        