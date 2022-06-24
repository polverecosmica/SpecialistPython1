# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
import random
n = int(input("enter the quantity "))
count = 1
str_output = []

while count <= n:
    str_temp = (random.randint(-100, 100))
    count += 1
    str_output.append(str_temp)

print(str_output)
