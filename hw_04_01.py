# объявление функции
def is_valid_password(password, total = 0, counter = 0):
    new_password = password.split(':')
    if len(new_password) > 3:
        counter -= 1
    a = new_password[0]
    b = new_password[1]
    c = new_password[2]
    if a == a[::-1]:
        counter += 1
    for i in range(2, int(b) + 1):
        if int(b) % i == 0:
            total += 1
    if total > 1 or int(b) == 1:
        counter -= 1
    else:
        counter += 1
    if int(c) % 2 == 0:
        counter += 1
    if counter == 3:
        return True
    else:
        return False
# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))