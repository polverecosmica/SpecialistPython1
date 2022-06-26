# Посчитайте количество согласных букв в данной строке.

text = str(input("enter your text here: "))

text = text.lower()
conson1 = ("БВГДЖЗЙКЛМНПРСТФХЦЧШЩ")
conson1 = conson1.lower()
count_cons = 0
for symbol in text:
    count = 0
    while count < len(conson1):
        if symbol == conson1[count]:
            count_cons += 1
            count += 1
        else:
            count += 1
print(count_cons)
