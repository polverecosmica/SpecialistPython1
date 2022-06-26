# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

text = input("enter your text: ")
count_point = 0
count_comma = 0
num = 0

count_point = text.count(".")
count_comma = text.count(",")
if count_point > count_comma:
    print("more points")
elif count_point < count_comma:
    print("more commas")
else:
    print("the same number of points and commas")
