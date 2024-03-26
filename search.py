# search.py

from game import GameState, Action, euclidean_distance
from utils import PriorityQueue

def a_star_search(initial_state):
    frontier = PriorityQueue()
    frontier.put(initial_state, 0)
    came_from = {}
    cost_so_far = {}
    came_from[initial_state] = None
    cost_so_far[initial_state] = 0

    while not frontier.empty():
        current_state = frontier.get()

        if is_goal_state(current_state):
            break

        for action in get_possible_actions(current_state):
            next_state = apply_action(current_state, action)
            new_cost = cost_so_far[current_state] + 1  # Custo uniforme para cada ação

            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                cost_so_far[next_state] = new_cost
                priority = new_cost + heuristic(next_state)
                frontier.put(next_state, priority)
                came_from[next_state] = current_state

    # Reconstruir o caminho a partir do estado objetivo
    path = []
    current_state = current_state
    while current_state is not None:
        path.append(current_state)
        current_state = came_from[current_state]
    path.reverse()

    return path

def is_goal_state(state):
    # Define a condição para o estado objetivo
    # Por exemplo, se a bola estiver na mesma posição que o jogador
    return state.player_position == state.ball_position

def get_possible_actions(state):
    # Retorna uma lista de ações possíveis a partir de um determinado estado
    # Por exemplo, mover-se em todas as direções possíveis
    actions = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:
                actions.append(Action(dx, dy))
    return actions

def apply_action(state, action):
    # Aplica uma ação a um estado e retorna o novo estado resultante
    new_player_position = (state.player_position[0] + action.dx, state.player_position[1] + action.dy)
    return GameState(new_player_position, state.ball_position)

def heuristic(state):
    # Heurística: Distância euclidiana entre a posição atual do jogador e a posição da bola
    return euclidean_distance(state.player_position[0], state.player_position[1], 
                              state.ball_position[0], state.ball_position[1])
