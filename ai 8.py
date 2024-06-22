class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()

        def dfs_recursive(node):
            visited.add(node)
            print(node, end=' ')

            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        dfs_recursive(neighbor)

        dfs_recursive(start)
        print()  # Print a newline after DFS traversal

# Example usage:
g = Graph()

# Adding edges to the graph
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Perform DFS traversal starting from vertex 2
print("DFS traversal starting from vertex 2:")
g.dfs(2)
