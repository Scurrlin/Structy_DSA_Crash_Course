# Write a function, tree_min_value, that takes in the root of a binary tree that contains number values.

# The function should return the minimum value within the tree.

# You may assume that the input tree is non-empty.

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# BF Solution
from collections import deque

def tree_min_value_bf(root):
    smallest = float("inf")
    queue = deque([root])
    
    while queue:
        current = queue.popleft()
        if current.val < smallest:
            smallest = current.val

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return smallest

# Time Complexity: O(n)
# Space Complexity: O(n)

# DF Solution
def tree_min_value_df(root):
    smallest = float("inf")
    stack = [root]
    
    while stack:
        current = stack.pop()
        if current.val < smallest:
            smallest = current.val

        if current.left is not None:
            stack.append(current.left)

        if current.right is not None:
            stack.append(current.right)

    return smallest

# Time Complexity: O(n)
# Space Complexity: O(n)

# Recursive solution
def tree_min_value_recursion(root):
    if root is None:
        return float("inf")
    
    min_left = tree_min_value_recursion(root.left)
    min_right = tree_min_value_recursion(root.right)

    return min(root.val, min_left, min_right)

# Time Complexity: O(n)
# Space Complexity: O(n)