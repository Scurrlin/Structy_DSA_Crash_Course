# Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

#BFS
from collections import deque

def has_path_bfs(graph, src, dst):
    queue = deque([src]) 
    
    while queue:
        current = queue.popleft()
        
        if current == dst:
            return True
        
        for neighbor in graph[current]:
            queue.append(neighbor)
    
    return False

# Time Complexity: O(n)
# Space Complexity: O(n)

#DFS

def has_path_dfs(graph, src, dst):

    stack = [src]
    while stack:
        current = stack.pop()
        
        if current == dst:
            return True
        
        for neighbor in graph[current]:
            stack.append(neighbor)
    
    return False

# Time Complexity: O(n)
# Space Complexity: O(n)

#Recursive Solution
def has_path_recursion(graph, src, dst):

    if src == dst:
        return True
    
    for neighbor in graph[src]:
        if has_path_recursion(graph, neighbor, dst) == True:
            return True
        
    return False

# Time Complexity: O(n)
# Space Complexity: O(n)