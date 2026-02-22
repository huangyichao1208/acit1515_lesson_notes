# """

# Review

# Creating Variables
# Converting Values in Variables
# Data Types
# Input and Output

# """

# # x = 10
# # y = str(10) 
# # y = "10"
# # print(type(y)) # string
# # y = int(y)  # getting the value of y, then converting to int, then setting
# # print(type(y))  # get the data type of y (returns int), then printed
# # name = "Hello, world"

# # password = input("Enter your password: ")  # Enter your password: _
# # # You entered purplemonkeydishwasher
# # print(password) # purplemonkeydishwasher
# # print('You entered ' + password)
# # print('You entered', password)
# # print(f'You entered {password}')

# # pwd = input('Please enter your password: ')

# # current_year = input('Please enter the year: ')
# # current_year = int(current_year) # conversion only works if the string is numeric (looks like a number, no alphabet or other characters)

# # To prevent possible crashes, we need to test values before converting

# """
# Conditional (if) Statements - allow us to run code conditionally (i.e. only run one or more lines if a condition evaluates to True)

# To write a conditional statement, use the 'if' keyword followed by a 'condition'

# A condition can be:
#     1. a comparison between two values
#     2. a test (function) that returns a boolean value
#     3. a boolean value
# """

# # current_year = input('Please enter the year: ')
# # strings have a method called isnumeric()
# # the isnumeric method MUST be attached by a period to a variable containing a string

# # if current_year.isnumeric():  # function that returns a boolean value
#     # any lines that are indented underneath an if statement are considered
#     # part of a conditional block
#     # any indented lines will only run if the condition resolves to True
#     # if the condition resolves to False, no indented lines are run

#     # Indentation must be consistent
#     # current_year = int(current_year)
#     # print(current_year)

# # the conditional block is considered done when the interpreter sees the first unindented the line
# # print('After the if statement')


# """
# Logical Operators

# comparison operators
# >       greater than
# <       less than
# >=      greater than or equal to
# <=      less than or equal to
# ==      equal
# !=      not equal
# and
# or
# not

# """

# # if final_grade >= 50:
# #     print('Say hello to Tom')

# # if final_grade <= 50:
# #     print('Say hello to Chris again')

# # if final_grade == 50:
# #     print('Say hello to Tom, but just barely')

# final_grade = 80
# has_exemption = True
# begging = True

# if final_grade < 50:
#     # if final_grade value is 40, then this 'block' runs, everything else is skipped
#     print('final_grade is less than 50')
#     print('Say hello to Chris again')
# elif has_exemption == True:
#     print('Say hello to Tom because you have prior coding experience')
# elif begging == True:
#     print('Maybe you will say hello to Tom but unlikely')
# else: 
#     # if the condition is false, i.e. final_grade is 50 or greater then the else block runs and the if block is skipped
#     print('Say hello to Tom')

# # VALID - but they are not related
# if final_grade < 50:
#     pass # pass is a placeholder

# if final_grade >= 50:
#     pass 

# """
# Rules for sets of related conditional statements:

# 1. start with a single mandatory if statement
# 2. followed by multiple optional elif statements
# 3. followed by single optional else statement

# NOTE: only one block can run - the first block that resolves to True

# VALID
# if ___:

# else:

# VALID
# if ____:

# elif ____:

# INVALID
# elif ____:

# else:

# INVALID:
# else:

# elif _____:
# """
# has_exemption = True

# if final_grade < 50:
#     # if final_grade value is 40, then this 'block' runs, everything else is skipped
#     print('final_grade is less than 50')
#     print('Say hello to Chris again')
# elif has_exemption: # has_exemption IS a boolean value, so no comparison is needed
#     print('Say hello to Tom because you have prior coding experience')

# print('After the conditional statements')

"""
ctrl-/ will comment/uncomment either the current line or all selected lines

if you need to change multiple instances of something (e.g. a variable name) select the word, then ctrl-d or cmd-d to get multiple cursors
or
hold the alt key and click on different lines to get multiple cursors
"""

# and, or, not

spends_all_money = True
buys_index_funds = True
buys_bitcoin = True

if not spends_all_money:
    print('You will get rich slowly')
elif buys_index_funds:
    print('You will get rich slowly')
elif not buys_bitcoin:
    print('You will get rich slowly')

if not spends_all_money and buys_index_funds and not buys_bitcoin:
    print('You will get rich slowly')

if spends_all_money or not buys_index_funds or buys_bitcoin:
    print('You may not get rich')

"""

AND

it is thursday and chris teaches 1515           T
it is friday and chris teaches 1515             F
chris teaches 1515 and it is friday             F
it is friday and chris is 10 feet tall          F

True AND True = True, otherwise False

OR

it is thursday or chris teaches 1515            T
it is friday or chris teaches 1515              T
chris teaches 1515 or it is friday              T
it is friday or chris is 10 feet tall           F

False OR False = False, otherwise True

"""

if age >= 16 and has_license and has_car:
    print('You can drive')

# Short-circuiting - if the value of a statement (multiple conditions) can be determined by one of the conditions, not all of the conditions are checked

age = 15
has_license = True
has_car = True

if age >= 16 or not (has_license and has_car):
    print('A')
else:
    print('B')

"""

Steps:
    Accept the invite

    In the terminal

    wsl ~ 
    (pick a folder)
    cd ~/Documents/1515
    eval $(ssh-agent -s)
    ssh-add ~/.ssh/acit1515
    git clone git@github.com:CIT-BCIT/b3-__________ assignment3


Assignment 3 hints:

at the top of your file import sys

import sys

if _______ or ______:
    sys.exit('Invalid input')


Part 2 (check if filename contains a slash)

response = input('Please enter a filename (blank for default): ')

# use the 'in' operator (to check for a character or characters in string)
if '/' in response:
    # not valid
"""
if 'CIT' in 'BCIT':
    print('Yes, CIT is part of BCIT')