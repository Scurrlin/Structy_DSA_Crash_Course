# Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1.

from collections import deque

def shortest_path(edges, node_A, node_B):

    visited = set()
    graph = make_graph(edges)
    queue = deque([ (node_A, 0) ])
    
    while queue:
        node, distance = queue.popleft()
        
        if node == node_B:
            return distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return -1 

def make_graph(edges):

    graph = {}
    for node1, node2 in edges:
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)
        graph[node2].append(node1)
    return graph

# Time Complexity: O(n)
# Space Complexity: O(n)