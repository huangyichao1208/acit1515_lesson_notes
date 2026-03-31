from random import randint
"""
Quiz Topics:
Sequences, For Loops

declare/create a list
read values from a list (multiple)
search for a value in a list
for loop (without range()) to loop through a sequence
for loop (with range()) to loop through a sequence
"""

# letters = ['a', 'b', 'c', 'd'] 
# # len(letters) -> 4, valid positions are 0 to 3
# # generally speaking, valid positions are always 0 to len() - 1

# print(letters[0])

# print(letters[3])
# print(letters[-1])
# print(len(letters) - 1) # prints 3
# print(letters[len(letters) - 1]) # prints 'd'
# print(letters[3])

# letters = ['a', 'b', 'c', 'd'] 
# print(letters[1:3]) # slice notation, start at 1 end at (3 - 1)
# print(letters[3:])

# print(letters[1])
# print(letters[2])


# letters = ['a', 'b', 'c', 'd'] 
# numbers = [1, 2, 3, 4]

# if 'c' in letters:
#     print('Found c!')

# if 2 in numbers:
#     print('Found 2')

# # no range(), the variable is going to contain the VALUE
# for letter in letters:     
#     print(letter)

# # with range(), the variable is going to contain A NUMBER/POSITION
# # using range(), print all the values from letters, one per-line

# # range(len(letters)) --> 0, 1, 2, 3
# # for i in range(4)
# for i in range(len(letters)):  
#     print(letters[i])

"""
Loops - repeat one or more statements (lines of code) n times automatically

    in a while loop, n depends on when a condition becomes false

    while False:            n = 0

    while True:             n = 1 to infinity

    while counter < 10:     if counter starts at 0 and 
                            counter is increased each 'iteration'
                            n = 10

    in a for loop, n is a fixed number

    n can be hardcoded -> for i in range(5)   n = 5
    
    n can be the length of a sequence -> for i in range(len(schools))
                                         n = the length of the sequence

                                         
Functions - run one or more statements (potentially) multiple times
            but a function runs on demand (not automatically)

            functions are named, reusable containers that execute a series of steps
"""
# response = input('Please enter your term: ')

# if response.isnumeric():
#     response = int(response)

#     if response < 1 or response > 4:
#         print('Invalid term')
#     else:
#         print('Thank you for the entering the term')

# response = input('Please enter your grade: ')

# if response.isnumeric():
#     response = int(response)

#     if response < 0 or response > 100:
#         print('Invalid grade')
#     else:
#         print('Valid grade')

# Instead of repeating the code for each time we need a value from the user, we can place
# it inside of a function

# create a function using the 'def' keyword followed by a name, followed by parentheses, followed by a colon

"""
validate_response:

1. gets input from a user
2. tests if the user input is numeric
3. convert user input to an integer
4. test if the integer is within a range
"""
# below is the function 'declaration' or 'definition' - it defines the steps
# BUT no code is run
def validate_response():
    response = input('Please enter your grade: ')

    if response.isnumeric():
        response = int(response)

        if response < 0 or response > 100:
            print('Invalid grade')
        else:
            print('Valid grade')

# when we want to run the steps inside the function we have to
# call/run/execute/invoke the function by referring to the function name and follow it with parentheses
# validate_response()    # everything inside validate_response() runs
# validate_response()    # everything inside validate_response() runs again

z = 10 # global scope - can be used everywhere (inside a function, outside)

# def average():
#     x = randint(0, 100) # declared inside the function, local scope
#     y = randint(0, 100) # declared inside the function, local scope
#     print(z) # global scope, ok to use inside the function
#     print(round((x + y) / 2))
    
# average()
# average()
# average()

# print(z) # OK

# print(x)    # ERROR, x is not defined, x belongs to the function

# IMPORTANT: any variables declared inside of a function can ONLY be used inside that function


"""
Inputs and Outputs for a function

To declare that a function accepts inputs, we need to declare 'parameters' - variables that belong to the function

Parameters are defined in the parentheses after the function name
separated by commas
"""
# def average(a, b):
#     # inside the function, a and b can be used like a variable (that belongs to the function), and we assign values to the parameters when we call the function
#     print(round((a + b) / 2))

# average(20, 80) # a = 20, b = 80  -> prints 50
# average(30, 90) # a = 30, b = 90  -> prints 60
# print(a, b) # ERROR, a and b are not defined outside the function

# average() # ERROR, missing 2 positional arguments
# average(10) # ERROR
# average(10, 20, 30) # ERROR

# print() # builtin function
# input() # builtin function

"""
Outputs

To output a value, we need the 'return' keyword

The return keyword:
1. it sends a value back to the line where the function was called (so that it can be used or stored in a variable)
2. it ends the function immediately

NOTES about 'return'

If you don't put a value after return, you return None

def f():
    return

result = f()
print(result)  # prints None

You can 'return' just about anything

def g():
    return print('Hello')

result = g()
print(result) # prints None

def h():
    return [1, 2, 3, 4]

def j():
    return (1, 2, 3) + (4, 5, 6)

"""
def average(a, b):
    # print((a + b) / 2)
    return (a + b) / 2
    print('Here?') # 'unreachable' code because return ends the function

result = average(80, 30) # if you need to get a value back from the function, i.e. put the function right-hand side of an assignment, you must use the 'return'
if result >= 50:
    print('Say goodbye to Chris')

# TEST
x = print('Hello')
print(x) # prints None - why? because print doesn't 'return' a value


def g(p1, p2):
    # p1 and p2 are called 'parameters'
    pass

g(10, 20) # 10 are 20 are 'arguments'
# arguments are assigned to parameters

# 'named' arguments
def j(p1, p2):
    print(p1 + p2)

j(10, 20) # assigned in order, p1 = 10, p2 = 20
j(p2 = 10, p1 = 20) # explicitly assigning values to the parameters by name, and the order does not matter

print('Hello') # print, by default, adds a newline
print('World')

print('Hello', end=' ') # overriding the default behaviour of print, add a space instead of a newline
print('World')

"""
Args and Kwargs
"""
def varargs(*args):
    # a parameter with a star before it (NOTE: only one can be declared) means the function will accept any number of arguments (0 or more)

    # NOTE: typically you do not use the * inside, just the variable name
    print(type(varargs)) # args is a tuple containing all of the values

varargs() # ()
varargs(1) # (1)
varargs(1, 2, 3) # (1, 2, 3)

def varargs(p1, p2, *args):  # this means the function accepts 2 or more arguments
    print(p1, p2, args)

varargs() # error
varargs(10, 20, 30, 40, 50) # p1 = 10, p2 = 30, args = (30, 40, 50)

def varargs(*args, **kwargs):
    # *args captures all the positional arguments in a tuple
    # **kwargs captures all the named (keyword) arguments in a dictionary

# varargs(10, 20, 30, a=1, b=2, c=3)  # args is a tuple (10, 20, 30)

