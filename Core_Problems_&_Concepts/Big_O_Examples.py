# O(1) => constant

# Example 1 
a = 4
sum = a + 10
print(sum)

# Example 2
str = "hello"
print(str[1])

# Example 3
stuff = { 'a': 1, 'b': 2, 'c': 3 }
print('b' in stuff)

# Example 4
stuff = { 'a': 1, 'b': 2, 'c': 3 }
print(stuff['b'])

# O(n) => linear

# Example 1
colors = ['red', 'blue', 'green', 'yellow', 'magenta']
print('green' in colors)

# Example 2
list = [5, 9, 2, -6, 12, 20, 30, 24]
sum = 0
for item in list:
    sum += item
print(sum)

# Example 3
sentence = "hello world, how are you?"
print(sentence.split(" "))

# Example 4
# Space: O(1)
def function2(n):
    for i in range(0, int(n/2)):
        print(i)

function2(20)

# Example 5
# Space: O(n)
def function3(n):
    nums = []
    for i in range(1, n):
        nums.append(i)
    return nums

print(function3(10))

# O(n^2) => polynomial

# Example 1
letters = ['a', 'b', 'c', 'd', 'e', 'f']
for letter1 in letters:
    for letter2 in letters:
        print(letter1 + ' ' + letter2)

# Example 2
# Space: O(n)
def function4(n):
    nums = []
    for i in range(1, n):
        nums.insert(0, i)
    return nums

print(function4(10))

# Example 3
# Space: O(n^2)
def function5(s):
    for char1 in s:
        for char2 in s:
            print(char1 + ',' + char2)
    
    for char1 in s:
        print(char1)

function5('qrs')