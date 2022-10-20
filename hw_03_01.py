s = input('Введите предложение из двух слов ').strip()
total = 0
a = ''
b = ''
for i in s:
    total += 1
    if i == ' ':
        a = s[: total]
        b = s[total:]
print(f'{b} ! {a}')

print('===' * 7)

s = input('Введите предложение из двух слов ').strip()
nomer_probela = s.find(' ')
print(s[nomer_probela + 1 :] + ' ! ' + s[:nomer_probela], sep='')

print('===' * 7)

s = input()
s.split('!')
print(str(s))


