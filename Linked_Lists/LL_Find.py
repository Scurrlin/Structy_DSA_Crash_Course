# Write a function, linked_list_find, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target.

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

def linked_list_find(head, target):
    current = head
    while current is not None:
        if current.val == target:
            return True
        current = current.next
    return False

# Time Complexity: O(n)
# Space Complexity: O(1)

# Recursive solution
def linked_list_find_recursion(head, target):
    if head is None:
        return False
    if head.val == target:
        return True
    return linked_list_find_recursion(head.next, target)

# Time Complexity: O(n)
# Space Complexity: O(n)