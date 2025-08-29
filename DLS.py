from collections import deque

def dls_iterative(graph, start, goal, limit):
    # stack holds (node, depth)
    stack = [(start, 0)]

    while stack:
        node, depth = stack.pop()
        print("Visiting:", node, "| Depth:", depth)

        if node == goal:
            print("Goal found:", node)
            return True

        if depth < limit:  # only expand if within limit
            for neighbor in graph[node]:
                stack.append((neighbor, depth + 1))

    print("Goal not found within depth", limit)
    return False
# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Search with limit=2:")
dls_iterative(graph, 'A', 'E', 2)

print("\nSearch with limit=1:")
dls_iterative(graph, 'A', 'E', 1)