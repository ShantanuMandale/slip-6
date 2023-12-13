from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_node, path = queue.popleft()

        if current_node == goal:
            return path

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None

if _name_ == "_main_":
    # Define the graph as an adjacency list
    graph = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1, 6, 7],
        4: [2, 8],
        5: [2],
        6: [3],
        7: [3],
        8: [4]
    }

    initial_node = 1
    goal_node = 8

    path = bfs(graph, initial_node, goal_node)

    if path:
        print(f"Path from {initial_node} to {goal_node}: {path}")
    else:
        print(f"No path found from {initial_node} to {goal_node}")
