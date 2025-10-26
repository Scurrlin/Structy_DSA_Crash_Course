# Write a function tribonacci that takes in a number argument, n, and returns the n-th number of the Tribonacci sequence.

# The 0-th and 1-st numbers of the sequence are both 0.

# The 2-nd number of the sequence is 1.

# To generate further numbers of the sequence, calculate the sum of previous three numbers.

# Solve this recursively.

def tribonacci(n: int) -> int:
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    trib_n = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    return trib_n

# Time Complexity: O(3^n)
# Space Complexity: O(n)

def tribonacci(n: int) -> int:
    memo = {}
    return _tribonacci(n, memo)

def _tribonacci(n: int, memo: dict[int, int]) -> int:
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    trib_n = _tribonacci(n - 1, memo) + _tribonacci(n - 2, memo) + _tribonacci(n - 3, memo)
    memo[n] = trib_n
    return memo[n]

# Time Complexity: O(n)
# Space Complexity: O(n)