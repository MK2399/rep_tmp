from random import randint
a = int(input('Введите первое число диапазона '))
b = int(input('Введите второе число диапазона '))
new_digit = randint(a, b)
digit = int(input('Введите число '))
flag = True
while flag == True:
    if digit == new_digit:
        flag = False
        print('Ты угадал')
    if digit != new_digit:
        print('Попробуй ещё раз')
        digit = int(input('Введите число '))
        continue
