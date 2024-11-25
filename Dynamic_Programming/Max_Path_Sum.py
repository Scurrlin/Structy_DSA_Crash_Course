# Write a function, max_path_sum, that takes in a grid as an argument. The function should return the maximum sum possible by traveling a path from the top-left corner to the bottom-right corner. You may only travel through the grid by moving down or right.

# You can assume that all numbers are non-negative.

# Recursive Solution

def max_path_sum(grid):

    return _max_path_sum(grid, 0, 0)

def _max_path_sum(grid, r, c):

    if r == len(grid) or c == len(grid[0]):
        return float("-inf")

    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c]

    down_path_sum = _max_path_sum(grid, r + 1, c)

    right_path_sum = _max_path_sum(grid, r, c + 1)

    return grid[r][c] + max(right_path_sum, down_path_sum)

# Time Complexity: O(2^n)
# Space Complexity: O(n)

# Memoization Solution

def max_path_sum(grid: list[list[int]]) -> int:

    return _max_path_sum(grid, 0, 0, {})

def _max_path_sum(grid: list[list[int]], r: int, c: int, memo: dict[tuple[int, int], int]) -> int:

    pos = (r, c)

    if pos in memo:
        return memo[pos]

    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return float("-inf")
    
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c]

    down_sum = _max_path_sum(grid, r + 1, c, memo)
    right_sum = _max_path_sum(grid, r, c + 1, memo)

    max_sum = grid[r][c] + max(down_sum, right_sum)

    memo[pos] = max_sum
    return memo[pos]

# Time Complexity: O(a * n)
# Space Complexity: O(a * n)