import numpy as np

def pso(func, bounds, num_particles=100, num_iterations=100):
    # Define la población de partículas y sus posiciones iniciales en el espacio de búsqueda
    particles = [np.random.uniform(bounds[0], bounds[1], size=2) for _ in range(num_particles)]
    velocities = [np.zeros(2) for _ in range(num_particles)]
    pbest = particles.copy()
    gbest = None

    # Aplica las reglas del algoritmo PSO para actualizar la posición de cada partícula
    for i in range(num_iterations):
        for j, particle in enumerate(particles):
            # Evalúa la función de costo en la posición actual de la partícula
            cost = func(particle)

            # Actualiza la mejor posición personal de la partícula si se encuentra un mejor valor
            if cost < func(pbest[j]):
                pbest[j] = particle

            # Actualiza la mejor posición global si se encuentra un mejor valor
            if gbest is None or cost < func(gbest):
                gbest = particle

        # Actualiza la velocidad y la posición de cada partícula
        for j, particle in enumerate(particles):
            print()
            velocities[j] = 0.5 * velocities[j] + 0.5 * (pbest[j] - particle) + 0.5 * (gbest - particle)
            particles[j] += velocities[j]

    # Devuelve la mejor posición encontrada
    return gbest

# Define la función de costo
def cost(x):
    return x[0] ** 2 + x[1] ** 2

# Ejecuta el algoritmo PSO para optimizar la función de costo
result = pso(cost, bounds=(-10, 10), num_particles=100, num_iterations=100)
print(result)
