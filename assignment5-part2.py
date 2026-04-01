from random import randint
import time

weeks = 16

print('Term Start')

course = ['ACIT1515', 'ACIT1620', 'ACIT1630', 'MATH1310']
# users can add more courses manually

scores = []

for c in course:
    scores.append([]) # create a nested lists

for i in range(weeks-1):

    for i1 in range(len(course)):
        scores[i1].append(randint(0,100)) # fill the nested lists

    print(f'Week {i+1} completed')
    time.sleep(0.5)

print('End of Term')

overall_total = 0 

for i in range(len(course)):

    total = 0

    for mark in scores[i]:
        total = total + mark # in this loop, get the sum of each course

    avg = round(total / len(scores[i])) # get the average of each course

    overall_total = overall_total + avg

    if avg < 50:
        print(f'{course[i]}: {avg}% (Fail)')
    else:
        print(f'{course[i]}: {avg}% (Pass)')

overall_avg = round(overall_total / len(course)) # get the overall average

if overall_avg < 50:
    print(f'You failed the term! Overall average: {overall_avg}%')
else:
    print(f'You passed the term! Overall average: {overall_avg}%')