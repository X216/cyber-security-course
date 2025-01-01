n = int(input('Enter the number : '))

if n < 0:
    print('Event or odd is not applicable')
elif n % 2 == 0:
    print(n, ' is a even')
elif n % 2 == 1:
    print(n, ' is a odd')
else:
    print('Wrong input')
