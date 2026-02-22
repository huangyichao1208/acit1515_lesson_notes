'''
midterm exam
2 hours - monday

rules:
you cannot be more than half an hour late.
on paper
assigned seating
only have writing utensils, water, snack, student id

two different versions of the exam

format:
short answer (similar to quiz questions)
    25 questions - 2 marks each
10 multiple choice - 1 mark each
    /60

topics:
no linux commands
no REPL (interactive python)
syntax errors/runtime errors
    sytax error = invalid codes
        (e.g. missing quotes, missing colon)
    runtime error = valid code, invalid operation 

'''

x = "hello"
x = True
print (type(x),x)
x = str (x)
age = input ("please enter an age: ")

sleeps = True
eats = False
drinks = True
if sleeps:
    print ("you will not feel tired")
elif not eats:
    print ("feel hungry")
elif drinks:
    print ("you will not feel thirsty")

if (sleeps or eats or drinks) == False:
    print ("terrible!")

password = ''
if password == '123456':
    print ("change your password")

term = input ("enter a value: ")
term = int (term)
if term > 4:
    print ("graduated")

if term.isnumeric() and int(term)>4:
     print ("graduated")

