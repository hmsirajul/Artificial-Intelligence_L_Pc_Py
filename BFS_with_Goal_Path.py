from collections import deque

def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])   # queue stores paths, not just nodes

    while queue:
        path = queue.popleft()    # take first path
        node = path[-1]           # last node in the path

        if node == goal:
            return path   # found path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = path + [neighbor]   # extend path
                queue.append(new_path)

    return None   # no path found

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS Path:", bfs_path(graph, 'A', 'E'))