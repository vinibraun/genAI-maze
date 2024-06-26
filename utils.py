import random

# Função de fitness
def fitness(path, maze, start, end):
    x, y = start
    for move in path:
        if move == 0 and x > 0 and maze[x - 1][y] == 0:  # Cima
            x -= 1
        elif move == 1 and x < len(maze) - 1 and maze[x + 1][y] == 0:  # Baixo
            x += 1
        elif move == 2 and y > 0 and maze[x][y - 1] == 0:  # Esquerda
            y -= 1
        elif move == 3 and y < len(maze[0]) - 1 and maze[x][y + 1] == 0:  # Direita
            y += 1

    return -(abs(end[0] - x) + abs(end[1] - y))  # Distância Manhattan negativa

# Gerar caminho aleatório
def generate_path(length):
    return [random.randint(0, 3) for _ in range(length)]

# Cruzamento
def crossover(parent1, parent2):
    point = random.randint(0, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

# Mutação
def mutate(path, mutation_rate):
    for i in range(len(path)):
        if random.random() < mutation_rate:
            path[i] = random.randint(0, 3)
    return path
