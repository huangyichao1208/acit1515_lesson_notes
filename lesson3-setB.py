from pathlib import Path

"""
Topics:

Command-Line (terminal) I/O
Variables (store data in a running program)
Data Types
Operators (symbols that have a special meaning in Python)
Debugging
Pathlib (Python library that allows us to interact with the filesystem)

Assignment 2:
    Creating some files/folders from a Python script
"""

"""
Recommended Workflow (in the terminal):
    create a folder in your wsl instance
        mkdir ~/Documents/week3
        or
        mkdir ~/Documents/ACIT1515/week3
    
    code ~/Documents/week3
        open the folder first, before editing the file, so that VSCode 
        is detecting the correct path

    create a file within VSCode
"""

print('Welcome') # Output - print() outputs values/text to the terminal

# input('Please enter the year: ') # Input - input() displays text to the user and then allows the user to enter a value

# Order of Operations
# anything inside of parentheses runs first
# input() runs, shows text to the user, and the value they enter becomes the argument to print
# print(input('Please enter the year: '))

# Instead of just printing the value the user enters, we normally store it in a variable

# Variable - a value (stored somewhere in memory) with a name (label) attached to it
# to create a variable, we need the 'assignment' operator, =

# Rules for variable names:
# they can contain numbers, letters, underscores
# they cannot start with a number
# they should not be a 'reserved' word (a reserved word is a word that is already used as part of the Python language)

# the right-hand side runs first, and the returned value is stored on the left-hand side of the assignment operator in the variable
# response = input('Please enter the year: ')  # creating a variable because it the first occurrence of the label 'response'

# print(response) # outputs the value of the variable. NOTE: no quotes around variable names
# print('response') # outputs the literal word 'response'

# response = 2027 # updating an existing variable
# response = input('') # updating an existing variable
# print(response)

# current_year = input('Please enter the year: ')
# # IMPORTANT: input() ALWAYS RETURNS A STRING (string is any sequence of characters inside of quotes) -> '2026'
# current_year = current_year + 1  # cannot add a string and number
# print(current_year)

"""
Syntax Errors - errors that occur as a result of invalid code

    print('Hello)     syntax error - unterminated string literal
    print('Goodbye')    never shown

    When you run a Python script, i.e.
        python3 assignment1.py

    there is a two-stage process. First, the file is checked for syntax errors. If any syntax errors are found, they are reported and the script is not executed. If no syntax errors are found, the script is run

Runtime Errors - valid code, but invalid (illegal) operations

    e.g. input() always returns a string, so if we need to perform any mathematical operation we would need to convert the value the user entered to a number
"""

"""
Data Types

str (any sequence of characters inside of single/double quotes)
response = input('...')

int (integer, whole numbers, e.g. 10, 20, 100, 1515)
x = 10

float (decimal numbers)
y = 10.5

bool (True, False) *python is case-sensitive
is_thursday = True

None (empty, doesn't exist)


Conversion Functions (convert from one compatible type to another)

str()
int()
float()
bool()
"""
year = input('Please enter the year: ')
print(year, type(year))
year = int(year)
print('Next year is', year + 1)  # Next year is 2027

"""
Operators (symbols that have a special meaning in Python)

=       assignment operator

mathematical 
+       addition AND 'concatenation' 
        (concatenation is joining two things together)
-       subtraction
*       multiplication
/       division
**      exponentiation    2**8
%       modulo (remainder)

shorthand
+=
-=
*=
/=
"""
print(10 % 2)   # 0, 2 goes into 10 exactly 5 times with nothing remaining
print(9 % 2)    # 1, 2 goes into 8 exactly 4 times, with one remaining
print(8 % 2)    # 0
print(7 % 2)    # 1
print(6 % 2)    # 0
# n % 2 tells you if n is even (0) or odd (1)

# Concatenation (joining two strings together)
year = "2026"
# print(year + 1)  # TypeError: can only concatenate str to str
print("It is " + year)  # outputs It is 2026

# On Thursday we study Python in ACIT1515 with Chris
day = "Thursday"
language = "Python"
program = "ACIT"
course = "1515"
instructor = "Chris"

print("On " + day + " we study " + language + " in " + program + course + " with " + instructor)

# Alternative to above using 'f' strings
# f-strings allow you to output value of variables/operations inside of a string
print(f"On {day} we study {language} in {program}{course} with {instructor}")

"""
NOTE: Python is 'weakly-typed' language - the data type of a variable can change

Debugging using print() and type()

type() tells you the current data type of a value stored in a variable
"""
x = 10
print(type(x)) # returns <class 'int'>, i.e. integer

x = "Akila"
print(type(x)) # returns <class 'str'>, i.e. string

x = True
print(x, type(x)) # print the value and the type - DO THIS OFTEN 

"""
Pathlib - filesystem library
    - create files/folders
    - navigate through the filesystem
    - list files/folders

Assignment 2: using Python to automate/script the creation of files/folders

Pathlib is part of Python, but is not enabled by default.
To use Pathlib we have to import it

from pathlib import Path
"""

# Path.home()  - your home directory

cwd = Path.cwd()  # this returns a Path object pointing to the current working directory (the folder that this script is in)
print(cwd)

# new_location = cwd.joinpath('test.txt')
new_location = cwd / 'test.txt'

# IMPORTANT: new_location is NOT a file or folder, it is just a path (i.e. location on your filesystem)

# create files at a given location using .touch()
new_location.touch()

# create folders at a given location using .mkdir()

# IMPORTANT: mkdir() and .touch() DO NOT TAKE ARGUMENTS, i.e. nothing goes inside the parentheses
# new_location.touch('test.txt') # DOES NOT WORK

"""
Path.cwd()
Path.home()
.touch() to create a file
.mkdir() to create a folder
"""
cwd = Path.cwd()                    # /home/student
new_location = cwd / 'src'          # /home/student/src
new_location.mkdir()

# new_location is the new 'src'
new_file_location = new_location / 'test.py'    # /home/student/src/test.py
new_file_location.touch()

"""
123456
password
pa55word
batman
jesus

haveibeenpwned.com

chris_harris@bcit.ca
chris_harris+_____@bcit.ca
chris_harris+hahaha@bcit.ca
chris_harris+amazon@bcit.ca
"""
