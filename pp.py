from random import randint
#randint (lower_bound, upper_bound)
temperature = []
days = 7
sum_tem = 0

for i in range (days):
    tem = randint (-30, 40)
    temperature.append(tem)

for i in range (len(temperature)):
    sum_tem = sum_tem + temperature[i]
    
avg_tem = sum_tem / len(temperature)
print ('the average temperature for the week is '+ str (avg_tem))