# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

num = 0
count_elements = len(names)
while num < count_elements:
    if num != count_elements - 1:
        print(f'{names[num]}, ', end="")
        num += 1
    else:
        print(f'{names[num]}')
        num += 1

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
