# Write a function fib that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

# The 0-th number of the sequence is 0.

# The 1-st number of the sequence is 1.

# To generate further numbers of the sequence, calculate the sum of previous two numbers.

def fib(n: int) -> int:

    memo = {}
    return _fib(n, memo)

def _fib(n: int, memo: dict[int, int]) -> int:

    if n == 0 or n == 1:
        return n

    if n in memo:
        return memo[n]

    fib_n =  _fib(n - 1, memo) + _fib(n - 2, memo)

    memo[n] = fib_n
    return memo[n]

# Time Complexity: O(n)
# Space Complexity: O(n)

# Recursive Solution
def fib(n: int) -> int:

    if n == 0 or n == 1:
        return n

    fib_n = fib(n - 1) + fib(n - 2)

    return fib_n

# Time Complexity: O(2^n)
# Space Complexity: O(n)