
# # # Function definition
# # def x():
# #     print ('Start')
# #     return # 1 return a value (None) 2. ends the function
# #     print ('End')

# # def x():
# #     print ('Start')
# #     return 10 # return the specified value, ending the function

# # x() # run the steps

# # def is_prime(num):
# #     if type (num) !=int:
# #         return False
    
# #     if num in [1,3,5,7, ...]:
# #         return True

# # def yell(message):
# #     return message + '!'
# # result = yell ('Hello')

# # def yell(message):
# #     print (f'{message}!')
# # yell ('Hello')

# # def add(lhs,rhs = 0):
# #     return lhs+rhs

# '''
# input() - to get values from the command-line
# print() - to output vales to the command-line

# please choose an option:
# 1 enter course
# 2 enter grade
# 3 view courses
# 4 view grades

# without 'persistence' (i.e. a database or a file)
# any data that the user enters is lost. When we re-run 
# the script, we are back to an empty 'state'
# '''

# '''
# File I/O (input and output)

# e.g. the same command-line app as above, but any courses or 
# grades that the user enters are stored in a file, and that 
# file is read when the program starts up

# '''

# '''
# python has low-level functions for writing to and reading from 
# files.

# file.open()
# file.close()

# but we are gping to use the 'with' syntax to simplify opening and closing files
# '''
# # with open() as f: #f is a variable name that you choose, which stores a reference to the file

# # open() takes two arguments
# #1. the string filename, e.g. a file called test.txt in the current
# #directory
# # 2. the (string) 'mode' - what do we intend to do with the file
# # (read? write? both?)

# '''
# (simple) modes:
#     'w' - write
#     'a' - append
#     'r' - read

# '''

# with open('test.txt','w') as file: #open the file test.txt in write mode
#     #'w' mode will create the file if it doesn't exist
#     file.write('Testing 123')

# with open('test.txt','w') as file: 
#     file.write('New line!\n')  # overwrites, 'w' modes 

# with open('test.txt','a') as file:
#     file.write ('Another new line!') # adds rather than overwrites

# # using 'with' means that we do not have to manually close the file

# '''
# aside:

# touch test        plain text file
# touch test.txt
# '''

# '''
# reading files using 'r' mode
# '''
# with open('test.txt','r') as file:
#     # reminder: the 'file' is an object represents the file
#     # data = file.read() # reads the entire file as a string
#     # print (data, type(data))
#     file.readlines() # return a list of strings (each line of the file)
#     '''
#     ['New line!', 'Another new line!']
#     '''
#     line = file.readline() # read juet the first line (returns a string)
#     line = file.readline() # read the next line (as a string)

# # while line := file.readling() != '': # walrus to the rescue
# #     print (line)

# #simpler version:
# for line in file:
#     print (line) #print adds a newline

# '''
# the above prints

# new line!

# another new line!

# why? because print adds a newline, but the existing line in the
# file already contains a newline
# '''

# '''
# practice:
# manually create a file, called numbers.txt, fill it with some numbers, one 
# per line

# e.g.
# 10
# 20
# 30
# 40

# read the file, print out the sum of the numbers
# '''

sum = 0

with open ('numbers.txt', 'r') as file:
    for line in file:
        sum = sum + int(line)

print (f'The result is {sum}')

from datetime import datetime

'''
Dates
'''

# get the current time (i.e. when the script runs)
today = datetime.now()
print (today)

# strftime() - format a date string
'''
strftime requires placeholders inside a string, e.g.

%Y   year
%m   month
%d   day
%A   day(human-readable name)

today.strftime('%Y')
today.strftime('%m %d, %Y')
today.strftime('%A %B %d, %Y')

'''

'''
calculating differences between dates
'''
today = datetime.now()
new_years = datetime (year = 2027, month = 1, day = 1) # Jan 1st, 2027

difference = new_years - today #returns a timedelta object
print (f'There are {difference.days} days until New Years')

'''
next week:

dictionaries (new data type)
JSON (plian text format for storing data)

'''
