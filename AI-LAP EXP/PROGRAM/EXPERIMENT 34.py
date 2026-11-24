
import random

# Objective function
def fitness(x):
    return x * x

# Initialize population
population = [random.randint(0, 31) for _ in range(6)]

# Genetic Algorithm
for generation in range(20):

    # Selection: choose the best individuals
    population.sort(key=fitness, reverse=True)
    parents = population[:3]

    # Crossover
    offspring = []
    for i in range(3):
        p1 = parents[i]
        p2 = parents[(i + 1) % 3]

        b1 = format(p1, '05b')
        b2 = format(p2, '05b')

        child = b1[:2] + b2[2:]
        offspring.append(int(child, 2))

    # Mutation
    for i in range(len(offspring)):
        if random.random() < 0.1:
            offspring[i] = random.randint(0, 31)

    population = parents + offspring

# Find best solution
best = max(population, key=fitness)

print("Best Solution (x):", best)
print("Maximum Fitness:", fitness(best))
print("Maximum Value of x:", best)
