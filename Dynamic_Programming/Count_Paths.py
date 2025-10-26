# Write a function, count_paths, that takes in a grid as an argument. In the grid, 'X' represents walls and 'O' represents open spaces. You may only move down or to the right and cannot pass through walls. The function should return the number of ways possible to travel from the top-left corner of the grid to the bottom-right corner.

# Recursive Solution
def count_paths(grid):
    return _count_paths(grid, 0, 0)

def _count_paths(grid, r, c):
    if r == len(grid) or c == len(grid[0]) or grid[r][c] == 'X':
        return 0
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1
    
    down_paths = _count_paths(grid, r + 1, c)
    right_paths = _count_paths(grid, r, c + 1)
    return down_paths + right_paths

# Time Complexity: O(2^n)
# Space Complexity: O(n)

# Memoization Solution
def count_paths_memo(grid: list[list[str]]) -> int:
    memo = {}
    return _count_paths_memo(grid, 0, 0, memo)

def _count_paths_memo(grid: list[list[str]], r: int, c: int, memo: dict[tuple[int, int], int]) -> int:
    pos = (r, c)
    if pos in memo:
        return memo[pos]
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 'X':
        return 0
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1

    down_paths = _count_paths(grid, r + 1, c, memo)
    right_paths = _count_paths(grid, r, c + 1, memo)
    total_paths = down_paths + right_paths
    memo[pos] = total_paths
    return memo[pos]

# Time Complexity: O(a * c)
# Space Complexity: O(a * c)