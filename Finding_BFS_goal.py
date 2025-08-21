
from collections import deque

def bfs_goal(graph, start, goal):
    queue = deque([start]) 
    visited = set()

    while queue:
        node = queue.popleft()  
        if node == goal:
            print(node)
            return True
        visited.add(node)

        for i in graph.get(node, []):
            if i not in visited and i not in queue:
                queue.append(i)  

    return False

graph = {
    "L": ["P", "C", "M"],
    "P": ["K", "R"],
    "C": ["N"],
    "M": ["Z"],
    "N": ["T"],
    "Z": ["Q"],
}

print(bfs_goal(graph, "L", "T"))
