# genAI-maze
Código em python de IA genética que resolve o melhor caminho de um labirinto.

# Projeto: Otimização de Caminhos em Labirintos

## Objetivo
Usar Algoritmos Genéticos para encontrar o caminho mais curto em um labirinto e visualizar o processo usando Pygame. A Distância Manhattan vai definir o melhor caminho matematicamente, e o algoritmo tentará seguir este caminho considerando os obstáculos e seus variados genes.

## Codificação de Solução
Codificação direta ou sequencial (mais provável ser a sequencial).

## Aplicações Reais
### Logística e Transportes
- Otimizar rotas de entrega para minimizar tempo ou custo de transporte.

### Navegação e Robótica
- Planejar o caminho de robôs em armazéns ou veículos autônomos em ambientes complexos.

### Desenvolvimento de Jogos
- Criar IA para NPCs (personagens não-jogadores) que possam navegar de maneira eficiente em ambientes complexos dentro de jogos.


## Escopo

### Definição do Labirinto
- Configurar o labirinto e suas características (dimensões, posições de início e fim).

### Implementação do Algoritmo Genético
- Representar soluções.
- Definir a função de aptidão (Distância Manhattan, pois o caminho só se dá por movimentos verticais e horizontais).
- Implementar operadores genéticos (cruzamento e mutação).
- Gerenciar a população e o ciclo de gerações.

### Visualização com Pygame
- Inicializar a janela do Pygame.
- Desenhar o labirinto e os caminhos.
- Atualizar a visualização a cada geração.

### Integração e Execução
- Integrar o Algoritmo Genético com a visualização em Pygame.
- Executar e ajustar parâmetros conforme necessário.

## Implementação do Algoritmo Genético

### Representação
Cada solução pode ser uma lista de movimentos (cima, baixo, esquerda, direita).

### Função de Aptidão
Medir a distância Manhattan do ponto final alcançado pelo caminho até o destino final. Penalizar colisões com paredes.

### Operadores Genéticos
- **Cruzamento:** Misturar partes de duas soluções.
- **Mutação:** Alterar movimentos aleatoriamente com uma pequena probabilidade.

### Gerenciamento da População
- Inicializar a população com soluções aleatórias.
- Avaliar a aptidão de cada solução.
- Selecionar soluções para reprodução.
- Gerar nova população através de cruzamento e mutação.

### Integração
Combinar o Algoritmo Genético com a visualização em Pygame e implementar um loop que executa o algoritmo e atualiza a visualização.


![Texto Alternativo](https://github.com/vinibraun/genAI-maze/blob/main/imagens/labirinto-img.PNG)
![Texto Alternativo](https://github.com/vinibraun/genAI-maze/blob/main/imagens/labirinto-resolvido-img.PNG)


## Pós Execução - Ajustes e Melhorias

### Ajustes
- Testar diferentes tamanhos de população e taxas de mutação.
- Ajustar o comprimento dos genes conforme a complexidade do labirinto.

### Melhorias
- Adicionar paredes e obstáculos ao labirinto.
- Melhorar a função de aptidão para considerar penalidades por colisões com paredes.
- Implementar técnicas de seleção mais sofisticadas, como torneio ou roleta.
