# Find the sum of an array using recursion.

def sum_numbers_recursive(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_numbers_recursive(numbers[1:])

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)