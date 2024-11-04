import random

n = random.randint(3,20)
print('Число из первой вставки: ', n)

def get_password(number):
    password = []
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password

result = get_password(n)
print('Пароль:', *result, sep='')