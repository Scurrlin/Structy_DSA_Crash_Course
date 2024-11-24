# What is Big-O Notation?

# Notation to describe the performance of algorithms
# Emphasis on how performance scales with input size

# Why use Big-O Notation?

# Allows us to compare performance of algorithms
# Does not rely upon environment (language, hardware, etc.)

# Big-O Simplification Rules

# Drop any constant factors
# Drop smaller terms in a sum

# Example with both rules:

# O(4n^2 + n + 5) => O(n^2)

# From Best to Worst

# 1.) O(1) => constant
# 2.) O(log(n)) => logarithmic
# 3.) O(n) => linear
# 4.) O(n^c): O(n^2), O(n^3) => polynomial
# 5.) O(c^n): O(2^n), O(3^n) => exponential
# 6.) O(n!) => factorial