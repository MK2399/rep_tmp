import math
def foo(digit : int):
    if digit < 0:
        print('Данное число отрицательное. Факториа́л — функция, определённая на множестве неотрицательных целых чисел.')
        return

    factorial = 1

    if digit == 0:
        print(f'Факториал равен {factorial}')
        return
    for i in range(digit, 0, -1):
        factorial *= i
    print(f'Факториал равен {factorial}')

foo(8)

print('===' * 7)

def new_foo(new_digit: int):
    if new_digit < 0:
        print('Данное число отрицательное. Факториа́л — функция, определённая на множестве неотрицательных целых чисел.')
        return

    new_factorial = 1

    while new_digit > 0:
        new_factorial *= new_digit
        new_digit -= 1
    print(f'Факториал равен {new_factorial}')


new_foo(-1)
