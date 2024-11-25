# Graphs = Nodes + Edges
# Any node that can be accessed from your current node by an edge is a neighbor

# BFS
from collections import deque

def breadth_first_print(graph, start):
    queue = deque([start])
    while len(queue) > 0:
        current = queue[0]
        print(current)
        queue.popleft()
        for neighbor in graph[current]:
            queue.append(neighbor)

# DFS
def depth_first_print(graph, start):
    stack = [start]
    while len(stack) > 0:
        current = stack[-1]
        print(current)
        stack.pop()
        for neighbor in graph[current]:
            stack.append(neighbor)

# Recursive
def depth_first_print_recursion(graph, current):
    print(current)
    for neighbor in graph[current]:
        depth_first_print_recursion(graph, neighbor)

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

depth_first_print(graph, "a")