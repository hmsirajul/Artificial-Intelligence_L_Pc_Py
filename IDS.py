from collections import deque

def dls_iterative(graph, start, goal, limit):
    """Depth-Limited Search (iterative, no path)"""
    stack = [(start, 0)]  # (node, depth)

    while stack:
        node, depth = stack.pop()
        print("Visiting:", node, "| Depth:", depth)

        if node == goal:
            print("Goal found at depth", depth)
            return True

        if depth < limit:
            for neighbor in graph[node]:
                stack.append((neighbor, depth + 1))

    return False


def ids(graph, start, goal, max_depth):
    """Iterative Deepening Search using iterative DLS"""
    for limit in range(max_depth + 1):
        print(f"\n--- Depth limit = {limit} ---")
        found = dls_iterative(graph, start, goal, limit)
        if found:
            print("Found within limit", limit)
            return True

    print("\nGoal not found up to max_depth", max_depth)
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

print("IDS search for 'E':")
ids(graph, 'A', 'E', max_depth=4)

