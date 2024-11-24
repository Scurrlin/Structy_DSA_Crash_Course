# Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

from collections import deque

def tree_includes(root, target):
    if root is None:
        return False
    
    queue = deque([ root ])

    while queue:
        current = queue.popleft()
        if current.val == target:
            return True
    
        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)
    
    return False

# Time Complexity: O(n)
# Space Complexity: O(n)

# Recursive solution

def tree_includes_recursion(root, target):
    if root is None:
        return False
    
    if root.val == target:
        return True
    
    return tree_includes_recursion(root.left, target) or tree_includes_recursion(root.right,target)

# Time Complexity: O(n)
# Space Complexity: O(n)