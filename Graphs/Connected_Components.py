# Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.

# DFS
def connected_components_count(graph):
    visited = set()
    count = 0
    
    for node in graph:
        if explore(graph, node, visited) == True:
            count += 1
        
    return count

def explore(graph, current, visited):

    if current in visited:
        return False

    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
        
    return True

# Time Complexity: O(n)
# Space Complexity: O(n)

# Recursive Solution
def connected_components_count(graph):

    visited = set()
    count = 0 
    
    def dfs(node):

        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    for node in graph:
        if node not in visited:
            dfs(node)
            count += 1
        
    return count

# Time Complexity: O(n)
# Space Complexity: O(n)