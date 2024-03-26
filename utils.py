import math
import heapq

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class PriorityQueue:
    def __init__(self):
        self.elements = []
        self.counter = 0  # Contador para garantir que os itens inseridos empatados tenham uma ordem determinística

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, self.counter, item))  # Adiciona um contador para garantir uma ordem determinística
        self.counter += 1

    def get(self):
        return heapq.heappop(self.elements)[2]  # Retorna o terceiro elemento da tupla, que é o item que estamos interessados
