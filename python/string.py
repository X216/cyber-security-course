# add two strings
print('hello' + ' jacky')

# Add new line and and qutation in string
print("This is a\nnew line's")

name = 'Rahim\n'
print(3 * name)  # print the name 3 times

# print multiple line of string
print(
    """
Hey This is me
Press F1 to continue
I am writing doc blocks
Python is easy
"""
)

# Dive into words
word = 'Bangladesh'
print(word[0])  # output: B
print(word[3])  # output: g
print(word[-1])  # output: h (starting from the last element)
print(word[-3])  # output: e (the 3rd element from last)
print(word[2:4])  # output: ng (from 2 to <4=3 index)
print(word[:6])  # output: bangla ( from start to <6 index)
print(word[6:])  # output: desh ( from 6 to end of the string)
print(len(word))  # output: 10 ( length of the string)
