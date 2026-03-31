"""
Functions - one or more statements that are assigned a name that we can run on-demand
"""

# Function definition
# def x():
#     z = 10 + 20
#     print('Start')
#     return # 1. return a value (None), 2. ends the function
#     print('End')
#     y = 2 + 3

# x() # run the steps

"""

def x():
    return    # returning None, ending the function

    return 10   # returning the specified value, ending the function
    return []
    return ''

"""

# def is_prime(num):
#     if type(num) != int:
#         return False
    
#     if num in [1, 3, 5, 7, ...]:
#         return True

# result = is_prime('Chris')

"""
Q1
"""
# def yell(message):
#     print(f'{message}!')
#     # print(message + '!')

# yell('Hello')

"""
Q2
"""
# def yell(message):
#     return message + '!'

# result = yell('Hello')
# print(result)

"""
Q3
"""
# parameters can have default arguments
# def add(lhs, rhs = 0):   
#     return lhs + rhs

# add(1, 2) # valid
# add(1)    # valid, lhs = 1, rhs = 0 (default)

"""
Q4

Only 'Start' is output because return ends the function
"""

"""
ASIDE:
"""
def y():
    return # returns None

def z():
    y = 10 + 10
    # without return keyword, None is returned

result = z()
print(result) # None

def f():
    # print() returns None
    # the line below is equivalent to return None (the output of the print() function)
    # return print('Hello')

    return 'akila'.upper()

# result = f()
# print(result)

"""
Week 12 (today): File I/O, Dates
Week 13: Dictionaries, JSON
Week 14: Sets and Strings
(OOP preview of next term - online notes)
Week 15: Review
Week 16: Exams
"""

"""
Previously we used
input() - to get values from the command-line
print() - to output values to the command-line

e.g. a command-line app that allows a user to enter courses and grades

Please choose an option:
1. Enter Course
2. Enter Grade
3. View Courses
4. View Grades

> 1

Please enter the course name:

> ACIT1515

Thank you for entering the course name

Please choose an option:
1. Enter Course
2. Enter Grade
3. View Courses
4. View Grades

Without 'persistence' (i.e. a database or a file) any data that the user enters is lost. When we re-run the script, we are back to an empty 'state'
"""

"""
File I/O (input and output)

e.g. the same command-line app as above, but any courses or grades that the user enters are stored in a file, and that file is read when the program starts up
"""

"""
Python has low-level functions for writing to and reading from files

file.open()
file.close()

but we are going to use the 'with' syntax to simplify opening and closing files
"""
# with open() as f:  # f is a variable name that you choose, which stores a reference to the file

# open() takes two arguments
# 1. the (string) filename, e.g. a file called test.txt in the current directory
# 2. the (string) 'mode' - what do we intend to do with the file (read? write? both?)

"""
(Simple) Modes:
    'w' - write         DANGER! - 'w' mode overwrites the file
    'a' - append
    'r' - read
"""
with open('test.txt', 'w') as file: # opening test.txt in write mode
    # 'w' mode will create the file if it doesn't exist
    file.write('Testing 123')

with open('test.txt', 'w') as file:
    file.write('New line!\n')

with open('test.txt', 'a') as file:
    file.write('Another new line!\n') # added to the file instead of overwriting because we are in 'a' append mode

# using 'with' means that we do not have to manually close the file

"""
ASIDE:

touch test              plain text file        
touch test.txt          plain text file
"""

"""
Reading files using 'r' mode
"""
with open('test.txt', 'r') as file:
    # reminder: the 'file' is an object represents the file
    # data = file.read()  # reads the entire file as a string
    # print(data, type(data))

    # lines = file.readlines()  # return a list of strings (each line of the file)
    """
    [ 'New line!', 'Another new line!' ]
    """
    # line = file.readline() # read just the first line (returns a string)
    # line = file.readline() # read the next line (as a string)

    # 
    # while file.readline() != '': # comparison is OK, but we're not storing the string that readline returns

    # while line := file.readline() != '':  # walrus to the rescue
    #     print(line)

    # simpler version: treat the file like a sequence
    for line in file:
        print(line)
    """
    The above prints

    New line!

    Another new line!

    Why? because print adds a newline, but the existing line in the file already contains a newline

    """

"""
Practice:

Manually create a file, called numbers.txt, fill it with some numbers, one per line

e.g.
10
20
30
40

Read the file, print out the sum of the numbers

with open('numbers.txt', 'r') as file:
    ...your solution here
"""
sum = 0

with open('numbers.txt', 'r') as file:
    for line in file:
        # sum = sum + int(line)
        print(line, end='')

print(f'The result is {sum}')


from datetime import datetime

"""
Dates
"""

# get the current time (i.e. when the script runs)
today = datetime.now()
print(today)

# strftime() - format a date string
"""
strftime requires placeholders inside a string, e.g.

%Y      year
%m      month
%d      day
%A      day (human-readable name)

today.strftime('%Y')                2026
today.strftime('%m %d, %Y')         03 26, 2026
today.strftime('%A %B %d, %Y')     Thursday March 26, 2026
"""

"""
Calculating differences between dates, e.g. how many days until new years
"""
today = datetime.now()
new_years = datetime(year = 2027, month = 1, day = 1) # Jan 1st, 2027

difference = new_years - today # returns a timedelta object
print(difference)
print(f'There are {difference.days} days until New Years')

"""
Next week:

Dictionaries (new data type)
JSON (plain text format for storing data)
"""

with open('numbers.txt', 'r') as f:
    # This is a 'list comprehension' - a shorthand version of the code below
    s = sum([int(line.strip()) for line in f.readlines()])

    # s = []
    # for line in f.readlines():
    #     s.append(int(line.strip()))
    # s = sum(s)