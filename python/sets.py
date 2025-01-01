# Set mainly hold unique elemets only
basket = {}  # This is wrong
basket = set()  # another way
basket = set({1, 2, 3, 4, 4, 4, 4})

print(basket)

# check if something is in the set
print(5 in basket)
print(3 in basket)
print(2 in basket)
