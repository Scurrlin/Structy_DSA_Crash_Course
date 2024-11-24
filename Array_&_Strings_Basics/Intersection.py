# Write a function, intersection, that takes in two lists, a & b, as arguments. The function should return a new list containing elements that are in both of the two lists.

def intersection(a, b):
    result = []
    items_set = set()

    for item_a in a:
        items_set.add(item_a)
    
    for item_b in b:
        if item_b in items_set:
            result.append(item_b)

    return result

# Time Complexity: O(n)
# Space Complexity: O(n)