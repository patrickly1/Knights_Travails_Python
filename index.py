from collections import deque

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_valid_moves(self):
        valid_moves = []
        moves = [[2, 1], [2, -1], [1, 2], [1, -2], [-2, 1], [-2, -1], [-1, 2], [-1, -2]]
        
        for dx, dy in moves:
            new_x = self.x + dx
            new_y = self.y + dy
            
            if 1 <= new_x < 9 and 1 <= new_y < 9:
                valid_moves.append((new_x, new_y))
        
        return valid_moves

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def find_shortest_path(self, start, end):
        queue = deque([start])
        visited = set()
        visited.add((start.x, start.y))
        parent_map = {}

        while queue:
            current = queue.popleft()
            
            if current.x == end.x and current.y == end.y:
                return self.construct_path(parent_map, start, end)
            
            for new_x, new_y in current.get_valid_moves():
                move = (new_x, new_y)
                if move not in visited:
                    visited.add(move)
                    queue.append(Node(new_x, new_y))
                    parent_map[move] = (current.x, current.y)
        
        return None

    def construct_path(self, parent_map, start, end):
        path = []
        current = (end.x, end.y)
        start_key = (start.x, start.y)

        while current != start_key:
            path.append(Node(*current))
            current = parent_map[current]
        
        path.append(start)
        path.reverse()
        return path

graph = Graph()
start = Node(1, 1)
end = Node(7, 7)
graph.add_node(start)

path = graph.find_shortest_path(start, end)
print([f"[{node.x},{node.y}]" for node in path])