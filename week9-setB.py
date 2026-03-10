"""
Topics:
While Loops
For Loops
Sequences

Next Week:
Quiz
Midterm
"""

# While Loops - repeat one or more lines of code until a boolean condition becomes False

"""
The boolean condition used in a while loop can be one of three types (just like in conditional statements):

1. a comparison
2. a function/operation that results in a boolean
3. a boolean
"""
counter = 0

# infinite loop
# while True:
#     print('Beginning of iteration')
#     counter = counter + 1 # counter += 1
#     print('End of iteration')

# while True:
#     response = input('Please enter the year: ')
#     if response.isnumeric():
#         print('Thank you for entering a year')
#         break # break forcibly stops the loop
#     print('Invalid value')

# print('Done')

# counter = 0

# while counter <= 10:
#     counter += 1
#     print(counter)

# response = input('Please enter the year: ')

# while not response.isnumeric():
#     print('Invalid input!')
#     response = input('Please enter the year: ')

#   :=    walrus operator
# while not (response := input('Please enter the year')).isnumeric():

"""
Next lab is lab 5 - you do not have a lab 4
Whatever mark you get for lab 5 will also be applied to lab 4

Lab 5 has two parts - simpler part A, more complicated part B

No more Pathlib
"""

# Sequences - new data types that allow you to store multiple values in a single variable

# Sequence Type 1: strings (sequence of individual characters)

x = 10
name = 'Akila'

# not a practical approach, time-consuming, what happens if there are 10,000 dogs or an unknown amount of dogs
dog1 = 'Charlie'
dog2 = 'Ron'
dog3 = 'Rocky'
dog4 = 'Frank'
dog5 = 'George'

# Sequence Type 2: List (array) - an ordered collection of mutable values
"""
Use square brackets to:
    declare/create a list (values separated by commas) on the right-hand side of the assignment operator
        dogs = ['Rocky', 'Frank', 'Ron']

    write values to a list when on the left-hand side of = and to the right of the list variable
        dogs[0] = 'George'  

    read values from a list when on the right-hand side of = (or in the absence of =) and to the right of a list variable
        
"""
dogs = ['Rocky', 'Frank', 'Ron']
print(type(dogs), dogs) # when you pass a variable storing a list to print() you will see all the values

dogs[0] = 'George'  # updating the value at position zero, replacing Rocky with George

print(dogs[0])

dog5 = dogs[0]

# RULE: any list stored in a variable can be followed by []

"""
Notes on lists: 
    - lists are 'mutable' (we can change the values inside the list)
    - lists can contain any type of mixed value
"""
mixed_list = [0, True, 'Chris', []]  # this list has length 4, contains an int, a boolean, a string, and a *nested (empty) list*

empty_list = []  # empty, but I can add values after declaring it

letters = ['a', 'b', 'c', 'd']
print(letters[1])   # b
# print(letters[4])   # ERROR - index out of bounds

# you can use negative indices
print(letters[-1])  # the last value, 'd'
print(letters[-2])  # the second last value, 'c'

# slice notation - allows you to grab a range of values
#   var[start:end]   start is included, end is excluded

# ASIDE: do not create variables called 'list'
print(letters[1:3])   # prints values at positions 1 to 2 (b and c)
print(letters[:2])    # prints values starting at zero (default) and go to 1, a and b
print(letters[1:])    # prints values starting at 1, going to the end, b c d

empty_list = []
# empty_list[0] = 'Rocky'  # Error! Out of bounds
empty_list.append('Rocky')  # .append() inserts values into the end of the list
empty_list.append('Frank')
empty_list.append('George')
print(empty_list) # ['Rocky', 'Frank', 'George']

# Sequence Type 2: Tuples (immutable) ordered collections of values

"""
Use ():
    - to declare/create a tuple when on the right-hand side of = 

Use []
    - to read a value from a tuple when on the right-hand side of = or in the absence of =
"""
numbers_tuple = (1, 2, 3, 4)
print(numbers_tuple[0])
num = numbers_tuple[-1]

# numbers_tuple[0] = 10  # Error! tuple does not support item assignment

# use a tuple any time you have values that should not change (accidentally or otherwise)
connection = ("localhost", 3306, "", "")

# e.g. reading, writing grades to a database/file
actions = [
    'List Grades',
    'Update Grade',
    'Quit'
]

"""
1. List Grades
2. Update Grade
3. Quit
"""

# ASIDE: be careful with tuples and parentheses
x = 'Douglas'       # string
x = ('Douglas')     # string
x = ('Douglas',)    # tuple!!

"""
enumerate() is a function that takes a list and returns a list of tuples, where each tuple is (index, value)

    options = ['List Grades', 'Update Grade', 'Quit']
            enumerate(options)
    [(0, 'List Grades'), (1, 'Update Grade'), (2, 'Quit')]
"""

# Sequence Operations - things that you can with any type of sequence (strings, lists, tuples)

# get the length of a sequence
numbers = [1, 2, 3, 4]
name = 'Douglas'
grades = (99, 100, 54, 78)

print(len(numbers)) # 4
print(len(name))    # 7
print(len(grades))  # 4

# concatenation
numbers = [1, 2, 3, 4]
more_numbers = [5, 6, 7, 8]
print(numbers + more_numbers) # [1, 2, 3, 4, 5, 6, 7, 8]

grades = (100, 99)
more_grades = (98, 90)
print(grades + more_grades) # (100, 99, 98, 90)

# NOTE: you can only concatenate the same type of sequence

# use the 'in' operator to test if a value is in a sequence
instructor = 'Chris'
grades = (100, 90, 80)

if 'r' in instructor:
    print('Found r')

if 100 in grades:
    print('wauw')

# count() the number of times a value appears
state = 'Mississippi'
print(state.count('s')) # returns 4, there are 4 's' in Misssissippi

# use index() to get the position of the first instance of a value in a sequence
print(state.index('s')) # prints 2

# NOTE: lists are the ONLY sequence type that you can .append() (because lists are immutable)
name = 'chris'          # strings are immutable
name = name.upper()     # strings can never be modified, so .upper() returns a new string

# For Loops - runs a set number of times (unlike a while loop which runs until a condition becomes False)

# We will use For Loops in two ways
# 1. loops through a sequence

name = 'Akila Ramani'
# print each character from name on its own line
# to read from a sequence, use square brackets with a numeric position
"""
A
k
i
l
a
...
"""
# for <variable_name> in <sequence>:
for character in name:
    # the word/symbol after for is the variable that will be assigned the values, it can be named any legal variable name

    # the 'character' variable will automatically be assigned the values from the sequence one-by-one, in order
    print(character)

# 2. use range() whenever we need a numeric index while we are looping 
# for <variable_name> in range(start:stop:step):

"""
range() gives you a sequence of numbers

for i in range(10):    10 is stop -> 0, 1, 2, 3, ... 9   stop is excluded!

for i in range(3, 10)   3 is start (included), 10 is stop (excluded)
                        3, 4, 5, 6, 7, 8, 9

for i in range(3, 10, 2)        3, 5, 7, 9

for i in range(10, -1, -1)      10, 9, 8, 7, ..., 0
"""
# write a for loop using range() that outputs 100 90 80 70 ... 0
for i in range(100, -1, -10):
    print(i)

# write a for loop using range() that outputs
# 2 4 8 16 32 64 128
# 2**n
# 1 2 3 4 5 6 7
for i in range(1, 8):
    print(2**i)

"""
Using range() with sequences
"""
firstname = 'Yichao'
# 0 - 5 are the valid positions (forwards)
# or -1 to -6 (backwards)

# OK, works, BUT you shouldn't ever hardcode a length
# for i in range(-1, -7, -1):

# e.g. printing firstname backwards
for i in range(len(firstname) - 1, -1, -1):
    # print(i) # incorrect, we want the value not the position
    print(firstname[i])  # first iteration i = 5, next i = 4


"""
In-class Example
"""
from random import randint

# randint(lower_bound, upper_bound)
# randint(-30, 40)  returns a random integer between -30 and 40

temperatures = []
total = 0  # store the average in this variable
days = 7

# for <variable> in <sequence>
# for i in range()
# .append()

# Use a for loop to insert 7 random values into the temperatures list
for i in range(days):    # 0 1 2 3 4 5 6
    # temp = randint(-30, 40)
    # temperatures.append(temp)
    temperatures.append(randint(-30, 40))

# Use a second for loop to iterate over the temperatures and calculate the average
# [-20, 12, 24, 16, -1, 5, 7]
for temperature in temperatures:
    total += temperature

print(f'The average for the week is {total / days}')

# Print the average temperature for the week

"""
Nested Sequences
"""
nested_list = [
    'a',
    'b',
    ['c', 'd', 'e'],
    'f'
]
# length of nested list? 4

# RULE: you can always follow a sequence with [] and a numeric

# print d?
print(nested_list[2][1])

# print a?
print(nested_list[0])

# print ['c', 'd', 'e']?
print(nested_list[2])

horrible_list = [
    [],
    [
        [
            'a',
            'b',
            ['c', 'd']
        ]
    ],
    []
]
print(horrible_list[1][0][2][1])
