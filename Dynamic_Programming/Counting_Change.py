# Write a function, counting_change, that takes in an amount and a list of coins. The function should return the number of different ways it is possible to make change for the given amount using the coins.

# You may reuse a coin as many times as necessary.

def counting_change(amount: int, coins: list[int]) -> int:
    return _counting_change(amount, coins, 0)

def _counting_change(amount: int, coins: list[int], idx: int) -> int:
    if amount == 0:
        return 1
    if amount < 0:
        return 0

    coin = coins[idx]
    total_ways = 0
    for qty in range(amount // coin + 1):
        remainder_amount = amount - (qty * coin)
        ways_for_remainder = _counting_change(remainder_amount, coins, idx + 1)
        total_ways += ways_for_remainder
    
    return total_ways

# Time Complexity: O(a^n)
# Space Complexity: O(n)