# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def neg_fibon(n):
    if n < 0:
        return (-1) ** (-n + 1) * neg_fibon(-n)
    if n in (1, 2):
        return 1
    return neg_fibon(n - 1) + neg_fibon(n - 2)


lst = []
num = int(input('Введите пожалуйста число '))
for i in range(-num, num + 1):
    lst.append(neg_fibon(i))
print(lst)