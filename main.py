from game import GameState
from search import a_star_search, heuristic

initial_state = GameState((0, 0), (5, 5)) 

priority = heuristic(initial_state)
print("Prioridade inicial:", priority)

path = a_star_search(initial_state)

print("Caminho encontrado pela busca A*:")
for state in path:
    print(f"Jogador: {state.player_position}, Bola: {state.ball_position}")