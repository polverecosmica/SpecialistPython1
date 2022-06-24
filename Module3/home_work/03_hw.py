# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
n = int(input("enter the quantity "))
count = 1
str_output = []
#the end of the first input
#
while count <= n:
    str_output.append(random.randint(-100, 100))
    count += 1
#the end of the first task
print(str_output) #for check
#
count = 0
sum_output = 0
#the end of the second input

while count < len(str_output):
    if str_output[count] > 0 and str_output[count]%2 == 0:
        sum_output += int(str_output[count])
        count += 1
    else:
        count = count + 1
print(sum_output)




