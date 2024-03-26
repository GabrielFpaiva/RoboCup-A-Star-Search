import math

class GameState:
    def __init__(self, player_position, ball_position):
        self.player_position = player_position
        self.ball_position = ball_position

class Action:
    def __init__(self, dx, dy):
        self.dx = dx 
        self.dy = dy  

class CostData:
    def __init__(self, actual_cost, estimated_cost):
        self.actual_cost = actual_cost
        self.estimated_cost = estimated_cost

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
