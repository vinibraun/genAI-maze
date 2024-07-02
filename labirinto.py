import pygame
import random
import sys

# Configurações do labirinto e da janela
WIDTH, HEIGHT = 400, 400
CELL_SIZE = 20
ROWS, COLS = 15, 15
START, END = (0, 0), (ROWS - 1, COLS - 1)
MAZE_WIDTH, MAZE_HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
MAZE_X = (WIDTH - MAZE_WIDTH) // 2
MAZE_Y = (HEIGHT - MAZE_HEIGHT) // 2

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (150, 150, 150)

# Representação do labirinto (0 = caminho livre, 1 = parede)
maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
]

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tech Challenge: Labirinto Genetico')

# Função para desenhar o labirinto
def draw_maze():
    screen.fill(BLACK)
    for x in range(ROWS):
        for y in range(COLS):
            if maze[x][y] == 1:
                pygame.draw.rect(screen, GRAY, (MAZE_X + y * CELL_SIZE, MAZE_Y + x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (MAZE_X + y * CELL_SIZE, MAZE_Y + x * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    pygame.draw.rect(screen, BLUE, (MAZE_X + START[1] * CELL_SIZE, MAZE_Y + START[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (MAZE_X + END[1] * CELL_SIZE, MAZE_Y + END[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Função de fitness
def fitness(path):
    x, y = START
    for move in path: # Basicamente, a movimentação tem que ser igual a 0 (espaço vazio), pois se for igual a 1, é um obstáculo, então ele não pode se mover ali
        if move == 0 and x > 0 and maze[x - 1][y] == 0:  # Cima
            x -= 1
        elif move == 1 and x < ROWS - 1 and maze[x + 1][y] == 0:  # Baixo
            x += 1
        elif move == 2 and y > 0 and maze[x][y - 1] == 0:  # Esquerda
            y -= 1
        elif move == 3 and y < COLS - 1 and maze[x][y + 1] == 0:  # Direita
            y += 1

    return -(abs(END[0] - x) + abs(END[1] - y))  # Distância Manhattan negativa (soma das diferenças absolutas entre as coordenadas x e y dos dois pontos)

# Gerar caminho aleatório
def generate_path():
    return [random.randint(0, 3) for _ in range(100)]

# Cruzamento
def crossover(parent1, parent2):
    point = random.randint(0, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

# Mutação
def mutate(path):
    for i in range(len(path)):
        if random.random() < 0.01:
            path[i] = random.randint(0, 3)
    return path

# Inicializar população
population = [generate_path() for _ in range(100)]

# Loop do Algoritmo Genético
for generation in range(1000):
    population = sorted(population, key=fitness, reverse=True)
    new_population = population[:50] # ELITE

    for _ in range(50):
        parent1, parent2 = random.choices(new_population, k=2)
        child = mutate(crossover(parent1, parent2))
        new_population.append(child)

    population = new_population

    # Visualizar melhor caminho
    best_path = population[0]
    score = fitness(best_path)
    print(f'Geração {generation + 1}: Melhor caminho com pontuação {score}')

    # Desenhar o melhor caminho
    screen.fill(BLACK)
    draw_maze()
    x, y = START
    for move in best_path:
        if move == 0 and x > 0 and maze[x - 1][y] == 0:  # Cima
            x -= 1
        elif move == 1 and x < ROWS - 1 and maze[x + 1][y] == 0:  # Baixo
            x += 1
        elif move == 2 and y > 0 and maze[x][y - 1] == 0:  # Esquerda
            y -= 1
        elif move == 3 and y < COLS - 1 and maze[x][y + 1] == 0:  # Direita
            y += 1
        pygame.draw.rect(screen, BLUE, (MAZE_X + y * CELL_SIZE, MAZE_Y + x * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    if score == -1:
        pygame.image.save(screen, 'captura_fim_labirinto.png')
        break

    pygame.display.flip()
    pygame.time.wait(300)

# Loop do Pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_maze()
    pygame.display.flip()


pygame.quit()
sys.exit()
