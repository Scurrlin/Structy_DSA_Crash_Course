# Write a function min_change that takes in an amount and a list of coins. The function should return the minimum number of coins required to create the amount. You may use each coin as many times as necessary.

# If it is not possible to create the amount, then return -1.

def min_change_recursion(amount:int, coins:list[int]) -> int:
    ans = _min_change_recursion(amount, coins)
    if ans == float('inf'):
        return -1
    return ans

def _min_change_recursion(amount:int, coins:list[int]) -> int:
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    
    min_coins = float('inf')
    for coin in coins:
        remaining_amount = amount - coin
        num_of_coins = 1 + _min_change_recursion(remaining_amount, coins)
        if num_of_coins < min_coins:
            min_coins = num_of_coins
            
    return min_coins

# Time Complexity: O(a^n)
# Space Complexity: O(n)

# Memoization Solution
def min_change_memo(amount: int, coins: list[int]) -> int:
    ans = _min_change_memo(amount, coins, {})
    if ans == float('inf'):
        return -1
    return ans

def _min_change_memo(amount: int, coins: list[int], memo: dict[int, int]) -> int:
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    min_coins = float('inf')
    for coin in coins:
        remaining_amount = amount - coin
        num_coins = 1 + _min_change_memo(remaining_amount, coins, memo)
        min_coins = min(min_coins, num_coins)
        
    memo[amount] = min_coins
    return memo[amount]

# Time Complexity: O(a * n)
# Space Complexity: O(n)