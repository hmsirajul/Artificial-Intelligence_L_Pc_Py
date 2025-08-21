from collections import deque

def bfs_path_goal(graph, start, goal):
    queue = deque([[start]]) 
    visited = set()
    
    while queue:
        path = queue.popleft()
        node = path[-1]

        print ("Path: ", path)
        
        if node == goal:
            #print ("Goal finded: ", path)
            return path
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph.get(node, []):
                new_path = path + [neighbor]
                queue.append(new_path)
    
    return False


graph = {
    "L": ["P", "C", "M"],
    "P": ["K", "R"],
    "C": ["N"],
    "M": ["Z"],
    "N": ["T"],
    "Z": ["Q"],
}

print(bfs_path_goal(graph, "L", "T"))       
