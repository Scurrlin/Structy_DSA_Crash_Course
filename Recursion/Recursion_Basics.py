# Recursion

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)

# Output

# 5
# 4
# 3
# 2
# 1

# Change print statement and countdown(n - 1) order

def countdown_v2(n):
    if n == 0:
        return
    countdown_v2(n - 1)
    print(n)

countdown_v2(5)

# Output

# 1
# 2
# 3
# 4
# 5

# Add additional print statement

def countdown_v3(n):
    if n == 0:
        return
    print("entering " + str(n))
    countdown_v3(n - 1)
    print("return from " + str(n))

countdown_v3(5)

# Output

# entering 5
# entering 4
# entering 3
# entering 2
# entering 1
# return from 1
# return from 2
# return from 3
# return from 4
# return from 5