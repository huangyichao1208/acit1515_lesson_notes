from random import randint
import time

weeks = 16

print ('Term Start')
scores = []
score_avg = 0
score_sum = 0

for i in range (weeks-1):
    scores.append (randint (0,100))
    print (f'Week {i+1} completed')
    time.sleep(0.5)
print ('End of Term')

for score2 in scores:
    score_sum = score_sum + score2

score_avg = score_sum / (weeks-1)
score_avg = round (score_avg)

if score_avg < 50:
    print (f'You failed! Your average score for the term is {score_avg}%')
else:
    print (f'You passed! Your average score for the term is {score_avg}%')


# Place your solution here