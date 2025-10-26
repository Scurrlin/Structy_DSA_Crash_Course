# Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

def depth_first_values(root):
    if root is None: return []
    values, stack = [], [root]

    while stack:
        current = stack.pop()
        print(current.val)

        if current.right is not None:
            stack.push(current.right)
        if current.left is not None:
            stack.push(current.left)
    
    return values

# Time Complexity: O(n)
# Space Complexity: O(n)

# Recursive solution
def depth_first_values_recursive(root):
    if root is None:
        return []
    
    left_values = depth_first_values_recursive(root.left)
    right_values = depth_first_values_recursive(root.right)
    return [ root.val, *left_values, *right_values ]

# Time Complexity: O(n)
# Space Complexity: O(n)