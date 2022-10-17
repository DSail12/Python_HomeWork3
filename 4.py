# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите пожалуйста число '))
resultat = ""
while number > 0:
    resultat = str(number % 2) + resultat
    number //= 2
    print(resultat)