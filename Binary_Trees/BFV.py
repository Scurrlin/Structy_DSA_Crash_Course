# Write a function, breadth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in breadth-first order.

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

def breadth_first_values(root):
    if root is None:
        return []

    values = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        values.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return values

# Time Complexity: O(n)
# Space Complexity: O(n)