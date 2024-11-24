# Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

def zipper_list(head1, head2):
    tail = head1
    current1 = head1.next
    current2 = head2
    count = 0

    while current1 is not None and current2 is not None:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next
        count += 1
    
    if current1 is not None:
        tail.next = current1
    if current2 is not None:
        tail.next = current2
    
    return head1


# Time Complexity: O(n)
# Space Complexity: O(1)

# Recursive solution
def zipper_list_recursion(head1, head2):
    if head1 is None and head2 is None:
        return None
    
    if head1 is None:
        return head2
    
    if head2 is None:
        return head1
    
    next1 = head1.next
    next2 = head2.next
    head1.next = head2
    head2.next = zipper_list_recursion(next1, next2)
    return head1

# Time Complexity: O(n)
# Space Complexity: O(n)