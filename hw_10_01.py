from math import sqrt

def calculator():
    while 1:
        c = input('Введите математический символ ')

        if c == 'sqrt':
            try:
                a = int(input('Введите число '))
            except ValueError:
                a = 0

        elif c in '+-/*^':
            try:
                a = float(input('Введите первое число '))
            except ValueError:
                a = 0
            try:
                b = float(input('Введите второе число '))
            except ValueError:
                b = 0

        if c == '+':
            print(f'{a} + {b} = {a + b}')

        elif c == '-':
            print(f'{a} - {b} = {a - b}')

        elif c == '*':
            print(f'{a} * {b} = {a * b}')

        try:
            if c == '/':
                print(f'{a} / {b} = {a / b}')
        except ZeroDivisionError:
            print('Деление на ноль недопустимо')

        if c == '^':
            print(f'{a} ^ {b} = {a ** b}')
        try:
            if c == 'sqrt':
                print(f'√a = {sqrt(a)}')
        except ValueError:
            print(f'Kорень из отрицательного числа извлечь нельзя')

        q = input('Хотите продолжить? yes/no ')
        if q == 'no':
            return ''


print(calculator())