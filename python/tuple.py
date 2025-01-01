# Example demonstrating tuple features
example_tuple = (1, 'Python', [3, 4], (5, 6))

# Accessing elements
print('Entire Tuple:', example_tuple)  # Output: (1, 'Python', [3, 4], (5, 6))
print('First Element:', example_tuple[0])  # Output: 1
print('Nested Tuple Element:', example_tuple[3][1])  # Output: 6

# Slicing the tuple
print('Sliced Tuple:', example_tuple[1:3])  # Output: ('Python', [3, 4])

# Modifying a mutable element inside a tuple (list)
example_tuple[2][0] = 99
print(
    'Modified Tuple:', example_tuple
)  # Output: (1, 'Python', [99, 4], (5, 6))
