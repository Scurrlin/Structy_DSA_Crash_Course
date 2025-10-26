# Write a function, non_adjacent_sum, that takes in a list of numbers as an argument. The function should return the maximum sum of non-adjacent items in the list. There is no limit on how many items can be taken into the sum as long as they are not adjacent.

# For example, given:

# [2, 4, 5, 12, 7]

# The maximum non-adjacent sum is 16, because 4 + 12. 4 and 12 are not adjacent in the list.

def non_adjacent_sum(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    
    include = nums[0] + non_adjacent_sum(nums[2:])
    exclude = non_adjacent_sum(nums[1:])
    return max(include, exclude)

# Time Complexity: O(2^n)
# Space Complexity: O(n)