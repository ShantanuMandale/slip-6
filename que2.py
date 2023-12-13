from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def bfs(self, start, goal):
        visited = set()
        queue = deque([start])

        while queue:
            current_node = queue.popleft()

            if current_node == goal:
                return True

            if current_node not in visited:
                visited.add(current_node)
                queue.extend(neighbor for neighbor in self.graph.get(current_node, []) if neighbor not in visited)

        return False

# Example graph
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(3, 7)
graph.add_edge(4, 8)
graph.add_edge(5, 8)
graph.add_edge(6, 8)
graph.add_edge(7, 8)

# Set the initial and goal nodes
initial_node = 1
goal_node = 8

# Run BFS algorithm
result = graph.bfs(initial_node, goal_node)

# Print the result
if result:
    print(f"There is a path from {initial_node} to {goal_node}.")
else:
print(f"No path found from {initial_node} to {goal_node}.")
