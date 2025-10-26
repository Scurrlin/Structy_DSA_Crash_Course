# Return the indices of the two values in an array that add up to the target.

def pair_sum(numbers, target_sum):
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return (i, j)

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def pair_sumv2(numbers, target_sum):
    previous_nums = {}
    for index, num in enumerate(numbers):
        complement = target_sum - num
        if complement in previous_nums:
            return (previous_nums[complement], index)
        previous_nums[num] = index

# Time Complexity: O(n)
# Space Complexity: O(n)