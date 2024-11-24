# Determine whether or not a number is a prime number.

def is_prime(n):

    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

# Time Complexity = O(n)
# Space Complexity = O(1)