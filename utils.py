import random

# Gerar caminho aleatório
def generate_path(length):
    return [random.randint(0, 3) for _ in range(length)]

# Cruzamento
def crossover(parent1, parent2):
    point = random.randint(0, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

# Mutação
def mutate(path, taxa_mutacao):
    for i in range(len(path)):
        numero_random = random.random()
        if numero_random < taxa_mutacao:
            path[i] = random.randint(0, 3)
            #print(f'SOFREU MUTAÇÃO - {taxa_mutacao}')
    return path