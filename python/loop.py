words = ['name', 'new', 'finding', 'best', 'nice']

for word in words:
    print('Length of ', word, ' word is : ', len(word))

# Deleting the inactive users with an object
users = {'Junayed': 'active', 'Jabir': 'inactive', 'Jobayer': 'active'}
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
# This will print the active users
print(active_users)

# Use range function
# range function can have 3 params. A single param n means 0 to n-1. Two params range(a,n) means from a to n-1. 3 params range(a,n,c) mean that it will start from a and end will n-1 and also increase by c

# 1 param range
for i in range(10):
    print(i, end=',')
print()
# 2 params range
for i in range(2, 10):
    print(i, end=',')
print()
# 3 params range
for i in range(2, 10, 2):
    print(i, end=',')
print()
# Printing the words list with range
for i in range(len(words)):
    print(words[i], end=',')
print()

# Break and continue. It will print the first two element
for i in range(len(words)):
    if i == 2:
        break
    print(words[i], end=',')
print()

# Break and continue. It will skip the element that have index 2
for i in range(len(words)):
    if i == 2:
        continue
    print(words[i], end=',')
print()

# we can use else statement with for loop. This will work like if/if/elif/ -> else
# Finding the prime numbers
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
