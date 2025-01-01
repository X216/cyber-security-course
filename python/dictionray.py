# dictionary works as key value pairs

# Example Dictionary
dic = {
    'name': 'Rohan',
    'age': 20,
    'rounds': [1, 2, 3],
    'points': [10, 20, 10],
}
print('# Original Dictionary:')
print(dic)

# Accessing Dictionary Elements
print('\n# Accessing Dictionary Elements')
print(dic['name'])  # Access using key
print(dic.get('age'))  # Access using get()
print(dic.get('non_existent_key', 'Default Value'))  # Get with default value

# Editing/Updating Values
print('\n# Editing/Updating Dictionary')
dic['age'] = 21  # Update value
dic['city'] = 'Dhaka'  # Add new key-value pair
dic.update(
    {'name': 'Rohan', 'country': 'Bangladesh'}
)  # Update multiple values
print(dic)

# Deleting/Removing Items
print('\n# Deleting/Removing Items')
removed_value = dic.pop('city')  # Remove key with pop()
print(f'Removed city: {removed_value}')
last_item = dic.popitem()  # Remove last item
print(f'Last removed item: {last_item}')
del dic['rounds']  # Remove key using del
print('After deletion:', dic)
dic.clear()  # Clear all items
print('Cleared dictionary:', dic)

# Reset the dictionary
dic = {
    'name': 'Rohan',
    'age': 20,
    'rounds': [1, 2, 3],
    'points': [10, 20, 10],
}

# Looping Through a Dictionary
print('\n# Looping Through Dictionary')
for key in dic:
    print(f'Key: {key}')
for value in dic.values():
    print(f'Value: {value}')
for key, value in dic.items():
    print(f'{key}: {value}')

# Nested Dictionary
print('\n# Nested Dictionary')
nested_dic = {
    'student1': {'name': 'Rohan', 'age': 20},
    'student2': {'name': 'Harish', 'age': 22},
}
print(nested_dic['student1']['name'])  # Access nested value
nested_dic['student3'] = {'name': 'Rafiq', 'age': 25}  # Add new nested item
for key, value in nested_dic.items():  # Loop through nested dictionary
    print(f'{key}: {value}')

# Dictionary Methods
print('\n# Dictionary Methods')
print('Keys:', dic.keys())  # Get all keys
print('Values:', dic.values())  # Get all values
print('Items:', dic.items())  # Get all key-value pairs
dic.update({'status': 'active'})  # Update dictionary
print('After update:', dic)
print("Pop 'points':", dic.pop('points'))  # Pop a key
print('Popitem:', dic.popitem())  # Pop last item
print('Clearing dictionary...')
dic.clear()  # Clear dictionary
print('Cleared dictionary:', dic)

# fromkeys() Method
keys = ['a', 'b', 'c']
new_dic = dict.fromkeys(keys, 0)  # Create dictionary with default values
print('\n# fromkeys Example:')
print(new_dic)

# End of Examples
print('\n# End of Dictionary Examples')
