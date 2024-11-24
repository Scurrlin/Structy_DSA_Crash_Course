# Return the indices of the two values in an array that produce the target when multiplied by each other.

def pair_product(numbers, target):
    prev_nums = {}

    for index, num in enumerate(numbers):
        complement = target / num

        if complement in prev_nums:
            return (prev_nums[complement], index)
        
        prev_nums[num] = index

# Time Complexity: O(n)
# Space Complexity: O(n)