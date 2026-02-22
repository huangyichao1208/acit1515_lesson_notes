from pathlib import Path
"""
Midterm Exam

2 Hours - Monday

Rules:
You cannot be more than half an hour late
You cannot leave for the first half hour
Only one person in the washroom at a time
Invigilator may accompany you to the washroom
Leave your phone with us when you go to the washroom
On Paper
Assigned Seating (check the desk in the TecHUB when you come in)
No earbuds/headphones, earplugs ok
No phone, laptop, bag, ONLY writing utensils, water, snack, student id
Place your bag on the right-hand side of the room before 

Two different versions of the exam

Format:
Short Answer (similar to quiz questions)
    Questions will be taken directly from the assignment warmup files
        assignment2-warmup.py

    20 questions - 2 marks each                 /40
    10 multiple choice - 1 mark each            /10
    /50

    Roughly 3-4 minutes per question
    Part marks will be given for questions
        0.5 mark will be deducted for each error

    e.g.
    Show all the code necessary to get a name from a user, storing it in a variable called response, then output a string in the form "Hello <name>" where name is the value of the response variable

    x = input('Please ...:')
    print(f'Hello {x}')  # f-string
    print('Hello ' + x)  # concatenation

    missing f at the beginning of the formatted string  -0.5
    did not use response for the variable name -0.5


Topics:
No linux commands
No REPL (interactive Python )
Syntax Errors vs Runtime Errors
    Syntax Error = invalid code
        (e.g. missing quotes, missing colon)
        syntax errors are detected before the script runs
    Runtime Error = valid code, invalid/illegal operation
        detected when the script is running
        e.g. 
        response = input('Please enter a year: ')
        response = int(response) # crash if response is not numeric
Command-line I/O
    print('') # output a hard-coded string
    print(response)  # output the value of a variable
    input('') # input
Pathlib
    e.g. create a folder called 'test' inside the home folder

    home = Path.home()
    folder_location = home / "test"
    folder_location.mkdir()

Variables
    = assignment operator
    valid variable name? 
        allowed characters: letters,numbers,_
        cannot start with a number
            _test123    VALID
            test_123    VALID
            123_test    INVALID
    
    x = 10
    x = "20"        OK? Yes

Data Types
    boolean         True/False
        Python is case-sensitive!!
    
        e.g. output the data type and the value of the x variable from the previous question

        print(type(x), x)
        print(type(x))          # int
        print(x)                # 1515

    int         10                  int()
    float       10.0                float()
    string                          str()
    boolean                         bool()
    None 

isnumeric()

Operators
    +, -, /, *
    =               assignment operator, Assigning/Storing
    ==              equality, Testing/Comparing
    !=              not equal
    not             not (negates/reverses a boolean value)

                    sick = True
                    print(not sick)       # False

                    2 + 3 * 4               # 14
                    (2 + 3) * 4             # 20

    >
    >=
    <
    <=
    and
    or


    NOT ON TEST
    :=          walrus operator

    CSS, NOT PYTHON
    * + *       lobotomized owl selector (selects every element that has a previous sibling)

        <div>
            <p></p>
            <p></p>         selected
            <p></p>         selected
        </div>

    e.g.
        create a variable called firstname and assign it a string
        create a second variable called lastname and assign it a string
        output "Hello <firstname> <lastname>" using concatenation (no f-string)

        firstname = "Akila"
        lastname = "Ramani"
        print("Hello" + firstname + lastname)  # HelloAkilaRamani
        print("Hello " + firstname + " " + lastname)
        print("Hello", firstname, lastname)    # shortcut, outputs each value with a space between them by default
Conditional (if) Statements

    A condition can be:
        sick = True

        boolean                 if sick:                sick IS a boolean
        comparison              if sick == True:        
        function                if getting_worse():     functions returns bool
                                if getting_worse() == True:

    Rules for grouped/related conditional statements

    1. start with a single, mandatory if

        if not sick:
            ....
        
        if isThursday:
    
        OK, but the two statements are not related

    2. followed by multiple, optional elif

        if not sick:
            ...
        elif <condition>:
            ...
        elif <condition>:

    3. followed by a single, optional else



studied = True
completed_labs = True
practiced_on_paper = True

INVALID, else must be last

if studied:
    ...
elif completed_labs:
    ...
else:
    ...
elif practiced_on_paper:

INVALID, only one else allowed

if studied:
    ...
else:
    ...
else:
    ...



studied = True
completed_labs = True
practiced_on_paper = True

Given these variables, write a (single) if statement (no else, no elif) that outputs "You will pass the exam" if all of the values are True

if studied and completed_labs and practiced_on_paper:
    print("You will pass the exam")

Write a statement that is logically equivalent using or instead of and

1. replace and with or

if studied or completed_labs or practiced_on_paper:
    print("You will not pass the exam")

2. put a not in front of all the conditions

if not studied or not completed_labs or not practiced_on_paper:
    print("You will not pass the exam")

3. change the output if necessary


"""

"""
https://hackmd.io/@charris17/python-language-quick-reference

() for the midterm refers to a function
print() - is a function that outputs text to the terminal
input() - is a function that gets input from a user and returns it

Where can functions go?

1. on the right-hand side of an assignment statement

response = input()      VALID

input() = ...    INVALID, never on the left-hand side

"""
cwd = Path.cwd()  # e.g. /home/raj/1515
folder_location = cwd / "test"  # e.g. /home/raj/1515/test
folder_location.mkdir() # mkdir does not return a value, so the None value is stored folder
print(type(folder1), folder1)  # None! thus you probably don't want mkdir() or touch() on the right-hand side of an equal sign

# change = make_change(20)  # returns bills
# give_away_money(20)  # does not return anything (tangible)


"""
Practice Questions
"""
1. Create a variable named x and assign a string to it

    x = "hello"

2. Update the x variable, assigning it a boolean value

    x = True

3. Output the data type and value of the x variable

    print(type(x), x)

4. Convert the value in x to a string, storing the result back in the x variable

    x = str(x)

5. Prompt a user to enter an age, store the result in a variable named age

    age = input('please....')

6. Given the following variables, write a single if statement and multiple elif statements (no else allowed) to output the following:

    If you sleep you will not feel tired
    If you eat you will not feel hungry
    If you drink you will not feel thirsty

    sleeps = True
    eats = True
    drinks = True

    if sleeps:
        print('not tired')
    elif not eats:
        print('hungry')
    elif drinks:
        print('not thirsty')

sleeps = True
eats = True
drinks = True

7. Write a single if statement that outputs "You will feel terrible" if all of the variables from the previous are not True

if (sleeps or eats or drinks) == False:
    print('feel terrible')

if not (sleeps or eats or drinks):
if not sleeps and not eats and not drinks

8. Given the variable below, write an if statement that checks if the password is equal to '123456'. If the password IS equal to '123456', output 'Please change your password'

password = ''

if password == '123456':
    print('Please change your password')


9. Prompt a user to enter a value, storing the value in a variable named 'term'. Write an if statement that outputs 'Graduated' if the value in term is greater than 4

term = input('Please....')
term = int(term)
if term > 4:
    print('Graduated')

if int(term) > 4:
    print('Graduated')

if term.isnumeric() and int(term) > 4:


10. True or False: the following is valid Python code:
Print('Hello World')

a) True
b) False