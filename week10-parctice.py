'''
functions!!
'''

'''
Loops repeat one or more statements in number of times

In a while loop, n is the number of times until a condition
becomes false

in a for loop, n is a set number, e.g. n is the length of a 
sequence, n is the sequence defined by range()
'''

'''
functions run one or more statements, but on demand (not 
automatically)
'''

response = input('please enter your age: ')
# if response.isnumeric():
#     response = int (response)
#     if response >=0 and response <=125:
#         print ('Thank you for entering your age')
#     else:
#         print('Age must be between 0 and 125')
# else:
#     print ('Age must be an integer')

# response = input('please enter your term: ')
# if response.isnumeric():
#     response = int (response)
#     if response >=0 and response <=4:
#         print ('Thank you for entering your term')
#     else:
#         print('Term must be between 1 and 4')
# else:
#     print ('THere must be an integer')

def validate_response():
    if response.isnumeric():
        response = int (response)
        if response >=0 and response <=4:
            print ('Thank you for entering your term')
        else:
            print('Term must be between 1 and 4')
    else:
        print ('THere must be an integer')