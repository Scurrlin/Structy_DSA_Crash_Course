# Write a function sum_possible that takes in an amount and a list of positive numbers. The function should return a boolean indicating whether or not it is possible to create the amount by summing numbers of the list. You may reuse numbers of the list as many times as necessary.

# You may assume that the target amount is non-negative.

def sum_possible(amount: int, numbers: list[int]) -> bool:
    if amount == 0:
        return True
    if amount < 0:
        return False

    for num in numbers:
        if sum_possible(amount - num, numbers):
            return True
        
    return False

# Time Complexity: O(n^a)
# Space Complexity: O(n)

def sum_possible(amount: int, numbers: list[int]) -> bool:
    return _sum_possible(amount, numbers, {})

def _sum_possible(amount: int, numbers: list[int], memo: dict[int, bool]) -> bool:
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return True
    if amount < 0:
        return False

    for num in numbers:
        remaining_amount = amount - num
        if _sum_possible(remaining_amount, numbers, memo):
            memo[amount] = True
            return True

    memo[amount] = False
    return memo[amount]

# Time Complexity: O(a * n)
# Space Complexity: O(a)