# Write a function, tree_sum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree.

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

from collections import deque

def tree_sum(root):
    if root is None:
        return 0
    
    total_sum = 0
    queue = deque([ root ])
    while queue:
        current = queue.popleft()
        total_sum += current.val

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return total_sum

# Time Complexity: O(n)
# Space Complexity: O(n)        

# Recursive solution
def tree_sum_recursion(root):
    if root is None:
        return 0
    return root.val + tree_sum_recursion(root.left) + tree_sum_recursion(root.right)

# Time Complexity: O(n)
# Space Complexity: O(n)