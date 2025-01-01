squares = [1, 4, 9, 16, 25]

print(squares)  # No need to any loop like c

# Same operation as strings
print(squares[0])  # First one
print(squares[-1])  # Last One
print(squares[-3])  # Third element from last
print(
    squares[:4]
)  # First four elements because start with 0 index and end with 3 ( <4 )
print(squares[2:4])  # From 2 index to less than 4 index ( < 4 = 3 )
print(squares[2:])  # From 2 index to end
print(squares[2:43])  # It will print from the 2 index to the end

# Adding two list
# We need a loop or for adding elements in array in c. But in python it is too easy like php
cubes = [1, 8, 27, 96, 5**3, 6**3]
squares = squares + cubes  # We have added cubes into the squares
print(squares)
# changing the elements
squares[3] = 20
print(squares[3])  # we have changed the third index element of the list

# We can use append to add character in the last
squares.append(10000)
print(squares[-1])  # Printing the last element and it must be 10000

# Replace a portion of a list
squares[2:5] = [10, 10, 10]
print(squares)  # index 2 to 4 (<5) value must be 10

# Replace the full list
squares[:] = []
print(squares)  # All elements are empty

# More on lists (Extra)
lis = [1, 2, 3]
lis.append(4)  # Append to the last
print('List after append', lis)
# insert(posittion, value)
lis.insert(len(lis), 'insert from insert function')
print('List after insert', lis)
#  remove the first item from the value which is equal to x .remove(x)
lis.remove('insert from insert function')
print('List after remove', lis)
# pop delete the last element
lis.pop()
print('List after pop', lis)
# appending more
lis.append(2)
lis.append(2)
# Count a value occurance
print(lis.count(2))
# Reverse a list
lis.reverse()
print(lis)
# Copy list
lis2 = lis.copy()
print(lis2)
