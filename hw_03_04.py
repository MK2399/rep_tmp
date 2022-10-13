print('Цикл for.')
digit = int(input('Введите число '))
total = 0
for i in range(1, digit + 1):
    total += i ** 3
print(total)
assert total not in range(0, -100)
print('====' * 7)

print('Цикл while.')
new_total = 0
new_digit = int(input())
while new_digit > 0:
    new_total += new_digit ** 3
    new_digit -= 1
print(new_total)

assert total not in range(0, -100)