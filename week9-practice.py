# while loops
'''
the boolean condition used in a while loop can
be one of three types 
1. a comparison
2. a function/operation that results in a boolean
3. a boolean
'''
# counter = 0

# # infinite loop
# while True:
#     print ('beginning of the iteration')
#     counter = counter+1 # counter+=1
#     print ('end of iteration')

# while True:
#     response = input ('please enter the year: ')
#     if response.isnumeric():
#         print ('thank you for entering')
#         break
#     print ('invalid value')

# print ('done')

counter = 0
while counter <= 10:
    counter +=1
    print (counter)
# 1-11

counter = 0
while counter <= 10:
    print (counter)
    counter +=1
# 0-10
response = input ('please enter the year: ')

while not response.isnumeric():
    print ('invalid input!')
    response = input ('please enter the year: ')

# := walrus operator 

# while (response := input ('please enter the year')).isnumeric():

'''
lab 5 is the next lab - we do not have a lab 4

no more pathlib
'''

# sequence type 1: strings (sequence of individual characters)

dog1 = 'charlie'
dog2 = 'ron'
dog3 = 'rocky'
dog4 = 'frank'
dog5 = 'george'

# list (array) 

dogs = ['rocky', 'frank', 'ron']
print (type(dogs), dogs)

dogs[0] = 'george'

'''
lists are mutable
can contain any type of mixed value
'''
mixed_list = [0, True, 'chris', []]

letters = ['a', 'b', 'c', 'd']
print (letters[1])

# you can use negative
print (letters[-1]) # d
print (letters[-2]) # c

# var[start:end]
#include start, exclude end
print (letters[1:3]) # position 1 to 2
print (letters[:2]) # prints cales at zero and go to 1, a and b
print (letters [1:]) # print values starting at 1, going to the end

empty_list = []
empty_list.append ('Rocky')
empty_list.append ('Frank')
empty_list.append ('George')
print (empty_list)

# tuples
# immutable
'''
use ():
    - to declare a tuple

use []
    - to read a value from a tuple
'''
numbers_tuple = (1,2,3,4) # i don't want it to change
print (numbers_tuple[0])
num = numbers_tuple[-1]
'''
enumerate
'''
# sequence operations (strings, lists, tuples)
# get the length of a sequence
numbers = [1,2,3,4]
name = 'Douglas'
grades = (99, 100, 54, 78)
print (len(numbers))
print (len(name))
print (len(grades))

#1 concatenation '+'
more_numbers = [5,6,7,8]
print (numbers + more_numbers)

#2 use 'in' operator - case sensitive
#3 count () the number of times a value appears
#4 use index () to get the position of the first instance
#5 .append() / .upper() / .lower()
#6 range() when we need a numeric index while we are looping

# for loops
'''
1 loops through a sequence
2 using range()

'''

for i in range (100, -1, -10):
    print (i)

for i in range (1,8):
    print (2**i)

'''
using range() with sequences
'''
firstname = 'Yichao'

'''
in-class example
'''

from random import randint
#randint (lower_bound, upper_bound)
temperature = []
total = 0
days = 7

for i in range (days):
    tem = randint (-30, 40)
    temperature = temperature.append(tem)
    i = i +1

for i in range (len(temperature)):
    sum_tem = sum_tem + temperature[i]
avg_tem = sum_tem / len(temperature)
print ('the average temperature for the week is '+ avg_tem)

'''
nested sequences
'''
