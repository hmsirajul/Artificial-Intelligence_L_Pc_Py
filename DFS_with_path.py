from collections import deque
def dfs_path(graph, start, goal):
    visited = set()
    stack = [[start]]   # stack stores paths

    while stack:
        path = stack.pop()   # take last path
        node = path[-1]

        if node == goal:
            return path   # found path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = path + [neighbor]
                stack.append(new_path)

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
print("DFS Path:", dfs_path(graph, 'A', 'E'))