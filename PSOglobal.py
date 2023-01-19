# Importamos las librerias necesarias
import random
import numpy as np

# Definimos nuestra función de optimización
def f(x):
    return x[0]**2 + x[1]**2

# Definimos la clase Particula que representa una partícula en el enjambre
class Particula:
    def __init__(self, x0):
        self.posicion = x0
        self.mejor_posicion_personal = x0
        self.velocidad = np.zeros(len(x0))
        
    def actualizar_velocidad(self, mejor_posicion_global):
        w = 0.5
        c1 = 0.8
        c2 = 0.9
        
        r1 = random.random()
        r2 = random.random()
        
        velocidad_cognitiva = c1 * r1 * (self.mejor_posicion_personal - self.posicion)
        velocidad_emocional = c2 * r2 * (mejor_posicion_global - self.posicion)
        self.velocidad = w * self.velocidad + velocidad_cognitiva + velocidad_emocional
        
    def actualizar_posicion(self, limites):
        self.posicion = self.posicion + self.velocidad
        self.posicion = np.clip(self.posicion, limites[0], limites[1])
        
    def actualizar_mejor_posicion_personal(self, fitness_func):
        nueva_fitness = fitness_func(self.posicion)
        if nueva_fitness > fitness_func(self.mejor_posicion_personal):
            self.mejor_posicion_personal = self.posicion
            
    def __str__(self):
        return " posicion: " + str(self.posicion) + " mejor posicion personal: " + str(self.mejor_posicion_personal) + " velocidad: " + str(self.velocidad)

# Definimos la clase Enjambre que representa un conjunto de partículas
class Enjambre:
    def __init__(self, fitness_func, limites, num_particulas):
        self.fitness_func = fitness_func
        self.limites = limites
        self.num_particulas = num_particulas
        self.particulas = []
        self.mejor_posicion_global = np.zeros(limites[0].shape)
        self.mejor_fitness_global = -1000000
        
        for i in range(self.num_particulas):
            posicion = np.random.uniform(low=limites[0], high=limites[1])
            particula = Particula(posicion)
