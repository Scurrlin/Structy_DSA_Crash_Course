# Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

def sum_list(head):
    total = 0
    current = head
    while current is not None:
        total += current.val
        current = current.next
    return total

# Time Complexity: O(n)
# Space Complexity: O(1)

# Recursive solution
def sum_list_recursion(head):
    if head is None:
        return 0
    return head.val + sum_list(head.next)

# Time Complexity: O(n)
# Space Complexity: O(n)