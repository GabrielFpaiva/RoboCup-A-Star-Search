from game import GameState
from search import a_star_search, heuristic

# Definir o estado inicial do problema
initial_state = GameState((0, 0), (5, 5))  # Posição inicial do jogador e da bola

# Chamar a função de avaliação f(x)
priority = heuristic(initial_state)
print("Prioridade inicial:", priority)

# Executar a busca A* para encontrar o caminho ótimo
path = a_star_search(initial_state)

print("Caminho encontrado pela busca A*:")
for state in path:
    print(f"Jogador: {state.player_position}, Bola: {state.ball_position}")