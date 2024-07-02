import pygame
import random
import sys
from utils import *
from desenhar_lab import *

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tech Challenge: Labirinto Genetico')

# Inicializar população
population = [generate_path(100) for _ in range(100)]

# Loop do Algoritmo Genético
last_scores = []
mutation_rate = 0.01 # Definindo taxa de mutação inicial
for generation in range(1000):
    population = sorted(population, key=fitness, reverse=True)
    new_population = population[:50] # Preserva os 50 melhores indivíduos (elitismo)

    for _ in range(50):
        parent1, parent2 = random.choices(new_population, k=2)
        # DÚVIDA: FAZ MAIS SENTIDO APLICAR MUTAÇÃO EM TODA CRIANÇA (NOVA POP) (IDEIA 1) OU APLICAR MUTAÇÃO SOMENTE QUANDO ELA NÃO SE ADAPTAR? (IDEIA 2)
        child = crossover(parent1, parent2) #child = mutate(crossover(parent1, parent2), mutation_rate) # MUDAR PARA ESTE CHILD SE A IDEIA 1 FOR A CORRETA
        if mutation_rate == 0.05:
            child = mutate(crossover(parent1, parent2), mutation_rate) # REMOVER ESTE IF CASO A IDEIA 1 SEJA A CORRETA
        new_population.append(child)

    population = new_population

    # Visualizar melhor caminho
    best_path = population[0]
    score = fitness(best_path)
    print(f'Geração {generation + 1}: Melhor caminho com pontuação {score}')
    
    # Atualiza a lista de scores
    last_scores.append(score)
    if len(last_scores) > 4:
        last_scores.pop(0)

    # Verifica se o score se repetiu 4 vezes (evitar estagnação)
    if len(last_scores) == 4 and last_scores.count(score) == 4:
        print("Score repetido 4 vezes, aplicando punição (mutação dos filhos)")
        # Aumenta a taxa de mutação temporariamente para diversificar a população (Diversificação Forçada)
        mutation_rate = 0.05
    else:
        mutation_rate = 0.01 # MANTER ESTE ELSE SOMENTE SE A IDEIA 1 PREVALECER, PRECISO ESCLARECER ESTA DÚVIDA

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
