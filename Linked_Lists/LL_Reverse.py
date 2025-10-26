# Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

# Time Complexity: O(n)
# Space Complexity: O(1)

# Recursive solution
def reverse_list_recursion(head, prev = None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverse_list_recursion(next, head)

# Time Complexity: O(n)
# Space Complexity: O(n)