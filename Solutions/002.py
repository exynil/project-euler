# Задача 2

# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

amount = 0
a = 0
b = 1
c = a + b
while c < 4000000:
    if c % 2 == 0:
        amount += c
    a = b
    b = c
    c = a + b
print(amount)