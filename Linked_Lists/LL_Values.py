# Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

def linked_list_values(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values

# Time Complexity: O(n)
# Space Complexity: O(n)

# Recursive solution
def linked_list_values_recursion(head):
    values = []
    store_values(head, values)
    return values

def store_values(head, values):
    if head is None:
        return
    values.append(head.val)
    store_values(head.next, values)

# Time Complexity: O(n)
# Space Complexity: O(n)
