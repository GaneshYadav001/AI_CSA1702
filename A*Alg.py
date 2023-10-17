import heapq
class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  
        self.h = 0  
        self.f = 0  
    def __lt__(self, other):
        return self.f < other.f
def get_neighbors(grid, node):
    neighbors = []
    row, col = node.position
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] != 1:
            neighbors.append(Node((new_row, new_col), node))
    return neighbors
def heuristic(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
def astar(grid, start, end):
    open_set = []
    heapq.heappush(open_set, start)
    closed_set = set()
    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.position == end.position:
            path = []
            cost = current_node.g  
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1], cost  
        closed_set.add(current_node.position)
        neighbors = get_neighbors(grid, current_node)
        for neighbor in neighbors:
            if neighbor.position in closed_set:
                continue
            tentative_g = current_node.g + 1  
            if neighbor not in open_set or tentative_g < neighbor.g:
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor.position, end.position)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.parent = current_node
                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)
    return None, 0  
grid = [[0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]]
start = Node((0, 0))
end = Node((4, 4))
path, cost = astar(grid, start, end)
print("Path:", path)
print("Cost:", cost)
