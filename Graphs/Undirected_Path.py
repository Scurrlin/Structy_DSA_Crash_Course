# Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.

# DFS
def undirected_path(edges, node_A, node_B):
    graph = build_graph(edges)
    return has_path(graph, node_A, node_B, set())

def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
    
    return graph

def has_path(graph, src, dst, visited):
    stack = [src]
    while stack:
        current = stack.pop()
        
        if current == dst:
            return True        
        if current in visited:
            continue
        
        visited.add(current)
        for neighbor in graph[current]:
            stack.append(neighbor)
    
    return False

# Time Complexity: O(n)
# Space Complexity: O(n)

# Recursive Solution

def undirected_path_recursion(edges: list[tuple[int, int]], node_A: int, node_B: int) -> bool:
    graph = build_graph(edges)
    return has_path(graph, node_A, node_B, set())

def build_graph(edges: list[tuple[int, int]]) -> dict[int, list[int]]:
    graph = {}
    for edge in edges:
        a, b = edge

    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

    return graph


def has_path(graph: dict[int, list[int]], src: int, dst: int, visited: set[int]) -> bool:
    if src == dst:
        return True
    if src in visited:
        return False

    visited.add(src)
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited) == True:
            return True

    return False

# Time Complexity: O(n)
# Space Complexity: O(n)    