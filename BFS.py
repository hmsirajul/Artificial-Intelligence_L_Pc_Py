from collections import deque 

def bfs(graph, start):
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            # print(node)
        for i in graph.get(node, []):
            if i not in visited:
                queue.append(i) 

    return visited 

    
   
    
graph = {
    "L": ["P", "C", "M"],
    "P": ["K", "R"],
    "C": ["N"],
    "M": ["Z"],
    "N": ["T"],
    "Z": ["Q"],
}

print(bfs(graph, "L"))
