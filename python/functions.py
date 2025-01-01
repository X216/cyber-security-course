def _():
    print('hello from _ function')


# Printing hello with function
_()
print('Printing Fibonacci with functions')


def fib(n):  # write Fibonacci series less than n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(10)
li = [10, 20, 30, 40]


def addToLi(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


li = addToLi(100, li)
print(li)


# Now we will see keyword arguments and positional arguments
# The first_name is only positional so you have to give this as a param
def greetings(first_name, last_name='Rahman', *, greeting):
    """The first_name is a positional argument, last_name has a default value,
    and greeting is a keyword-only argument."""
    print(first_name, last_name, greeting)


greetings('Harish', greeting='Hello')
greetings('Harish', 'Rafiq', greeting='Hi by using positional arguments')
greetings('Rohan', greeting='hello by using keyword arguments')
