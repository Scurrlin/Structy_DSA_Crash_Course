# Find the maximum value in an array.

def max_value(nums):
    maximum = float("-inf")

    for num in nums:
        if num > maximum:
            maximum = num
    
    return maximum

# Time Complexity = O(n)
# Space Complexity = O(1)