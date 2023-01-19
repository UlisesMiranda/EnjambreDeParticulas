import random
import numpy as np

class GPSO:
    def __init__(self, func, bounds, num_particles=100, num_iterations=100):
        self.func = func
        self.bounds = bounds
        self.num_particles = num_particles
        self.num_iterations = num_iterations

        # Define la población de partículas y sus posiciones iniciales en el espacio de búsqueda
        self.particles = [np.random.uniform(bounds[0], bounds[1], size=2) for _ in range(num_particles)]
        self.velocities = [np.zeros(2) for _ in range(num_particles)]
        self.pbest = self.particles.copy()
        self.gbest = None

    def optimize(self):
        
        file = open("Resultados.txt", 'w')
        
        # Aplica las reglas del algoritmo GPSO para actualizar la posición de cada partícula
        for i in range(self.num_iterations):
            file.write(f"Iteracion {i}:")
            for j, particle in enumerate(self.particles):
                
                a = 0.8
                b1 = 0.7
                b2 = 1
                
                r1 = random.random()
                r2 = random.random()
                
                # Evalúa la función de costo en la posición actual de la partícula
                cost = self.func(particle)

                # Actualiza la mejor posición personal de la partícula si se encuentra un mejor valor
                if cost < self.func(self.pbest[j]):
                    self.pbest[j] = particle

                # Actualiza la mejor posición global si se encuentra un mejor valor
                if self.gbest is None or cost < self.func(self.gbest):
                    self.gbest = particle

            # Actualiza la velocidad y la posición de cada partícula
            for j, particle in enumerate(self.particles):
                file.write(f"\nParticula {j}: ")
                file.write("Posicion: " + str(particle) + " Pbest: " + str(self.pbest[j]) + " PGlobal: "+ str(self.gbest) + " Velocidad: " + str(self.velocities[j]) )
                
                self.velocities[j] = (a * self.velocities[j]) + (b1 * r1 * (self.pbest[j] - particle)) + (b2 * r2 * (self.gbest - particle))
                self.particles[j] += self.velocities[j]
                
            file.write("\n\n-------------------------------------------------------------------------------------------------------------------------------------------\n\n")        
        file.close()
        # Devuelve la mejor posición encontrada
        return self.gbest

# Define la función de costo
def cost(x):
    return x[0] ** 2 + x[1] ** 2

# Crea una instancia de la clase GPSO
g = GPSO(cost, bounds=(-5, 5), num_particles=20, num_iterations=50)

# Ejecuta el algoritmo GPSO para optimizar la función de costo
result = g.optimize()
print("\nMEJOR POSICION GLOBAL:", result)
