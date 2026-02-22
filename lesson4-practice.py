# pwd = input ("please enter your password: ")

#the string is numeric 

#to prevent possible crashes, we need to test values before converting

'''
conditional statements - allow us to run code conditionally

to write a conditional statement, use the 'if' keyword 

a condition can be:
    1. a comparision between two values
    2. a test (function) that returns a boolean value
    3. a boolean value
'''
current_year = input ("please enter the year: ")
# strings have a method called isnumeric()
# the isnumeric method must be attached by a period to a variable 

'''
if current_year.isnumeric(): #function that returns a boolean value
    # any lines that are indented underneath an if statement are considered
    #part of a conditional block
    #any intented lines will only run if the conditon resolves to true
    #if the condition resolves to false, no indented lines are run
    current_year = int (current_year)
    print (current_year)
'''

'''
logical operators

comparison operators
>
<
>=
<=
==
!=
and
or
not

'''

'''
final_grade = 80
if final_grade >= 50:
    print ('Say hello to Tom')

if final_grade <=50:
    print ('say hello to chris again')

if final_grade == 50:
    print('say hello to tom, but just barely')
'''

final_grade = 80
has_exemption = True

if final_grade <=50:
    #if final_grade value is 40, then this 'block' runs, everything else is skipped
    print ('say hello to chris again')
    print ('final_grade is less than 50')

elif has_exemption == True:
    print ('say hello to tom because you have prior coding experience')

else:
    print ('say hello to tom')

'''
rules for sets of related conditonal statements:
2 start with a single mandatory if statement


'''

'''
final_grade = 80
has_exemption = True

if final_grade <=50:
    #if final_grade value is 40, then this 'block' runs, everything else is skipped
    print ('say hello to chris again')
    print ('final_grade is less than 50')

elif has_exemption: #this is the simplest one, it is already a boolean value
# so no comparison is needed
    print ('say hello to tom because you have prior coding experience')

else:
    print ('say hello to tom')
'''

# wpd = input('please enter your password: ')

# if len(wpd)>=8:
#     print('you entered',wpd)

spends_all_money = True
buys_index_funds = True
buys_bitcoin = True

if not spends_all_money:
    print ('you will get rich slowly')
elif buys_index_funds:
    print ('you will get rich slowly')
elif not buys_bitcoin:
    print('you will get rich slowly')

if not spends_all_money and buys_index_funds and not buys_bitcoin:
    print('you will get rich slowly')

if spends_all_money or not buys_index_funds or buys_bitcoin:
    print('you may not get rich')


'''

AND

it is Thursday and chris teaches 1515

'''

age = 15
has_license = True
has_car = True

if age >=16 and has_license and has_car:
    print ('you can drive')

#and&and: short-circuiting - if the value of a statement (multiple conditions) can be 
#determined by one of the conditions, not all of the conditions are checked

if age>= 16 or (has_license and has_car):
    print ('A')
else:
    print ('B')










