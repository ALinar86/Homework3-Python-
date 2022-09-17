# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def dec2bin():
    n = int(input())
    b = ''
    while n > 0:
        b += str(n % 2)
        n = n // 2
    return b


def reversed(variable):
    res = ''
    for i in range(len(variable)-1, -1, -1):
        res += variable[i]
    print(res)


reversed(dec2bin())
