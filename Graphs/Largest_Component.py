# Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.

# DFS
def largest_component_dfs(graph: dict[int, list[int]]) -> int:
 
    visited = set()
    max_size = 0

    for node in graph:
        if node not in visited:
            size = explore_size(graph, node, visited)
            max_size = max(max_size, size)

    return max_size

def explore_size(graph: dict[int, list[int]], node: int, visited: set[int]) -> int:

    stack = [node]  
    size = 0

    while stack:
        current = stack.pop()
        if current in visited:
            continue
      
        visited.add(current)
        size += 1
 
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)

    return size

# Time Complexity: O(n)
# Space Complexity: O(n)

# Recursive Solution
def largest_component_recursion(graph: dict[int, list[int]]) -> int:

    visited = set()
    largest = 0

    for node in graph:
        size = explore_size(graph, node, visited)
        if size > largest:
            largest = size

    return largest

def explore_size(graph: dict[int, list[int]], node: int, visited: set[int]) -> int:

    if node in visited:
        return 0

    visited.add(node)

    size = 1
    for neighbor in graph[node]:
        size += explore_size(graph, neighbor, visited)

    return size

# Time Complexity: O(n)
# Space Complexity: O(n)