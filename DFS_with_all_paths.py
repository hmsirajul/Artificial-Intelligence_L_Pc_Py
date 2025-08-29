from collections import deque
def dfs_path(graph, start, goal):
    visited = set()
    stack = [[start]]   # stack stores paths

    while stack:
        path = stack.pop()   # take last path
        node = path[-1]

        print("Popped path:", path)

        if node == goal:
            print("Goal found! Final path:", path)
            return path   # found path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = path + [neighbor]   # extend path
                print(f"  Extending {path} with {neighbor} → {new_path}")
                stack.append(new_path)
            print("Stack now contains:", stack)

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

print("DFS Path Search:")
dfs_path(graph, 'A', 'E')

