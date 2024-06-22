import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state  # Current state of the node
        self.parent = parent  # Parent node in the path
        self.g = g  # Cost from start to current node
        self.h = h  # Heuristic estimate from current node to goal
    
    def f(self):
        return self.g + self.h
    
    def __lt__(self, other):
        return self.f() < other.f()

def astar(start_state, goal_state, neighbors_func, heuristic_func):
    open_set = []
    closed_set = set()
    
    start_node = Node(start_state, g=0, h=heuristic_func(start_state, goal_state))
    heapq.heappush(open_set, start_node)
    
    while open_set:
        current_node = heapq.heappop(open_set)
        
        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]
        
        closed_set.add(current_node.state)
        
        for neighbor_state in neighbors_func(current_node.state):
            if neighbor_state in closed_set:
                continue
            
            g = current_node.g + 1  # Assuming uniform cost for simplicity
            h = heuristic_func(neighbor_state, goal_state)
            neighbor_node = Node(neighbor_state, parent=current_node, g=g, h=h)
            
            if any(node.state == neighbor_state and node.f() < neighbor_node.f() for node in open_set):
                continue
            
            heapq.heappush(open_set, neighbor_node)
    
    return None  # No path found

# Example usage:
def neighbors(state):
    x, y = state
    possible_neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]  # Assuming 4-connected grid
    return [neighbor for neighbor in possible_neighbors if 0 <= neighbor[0] < 5 and 0 <= neighbor[1] < 5]  # Boundaries

def manhattan_distance(state, goal_state):
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

start = (0, 0)
goal = (4, 4)
path = astar(start, goal, neighbors, manhattan_distance)

if path:
    print("Path found:", path)
else:
    print("No path found")
