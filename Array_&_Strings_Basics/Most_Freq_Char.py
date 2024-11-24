# Determine what the most frequent character is in a string. If there is a tie, return the character that appears first in the string.

def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        
        count[char] += 1
    
    most = None
    for char in s:
        if most is None or count[char] > count[most]:
            most = char
    return most

# Time Complexity: O(n)
# Space Complexity: O(n)
