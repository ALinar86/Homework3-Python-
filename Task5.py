# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0 , 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи](https://clck.ru/yWbkX.)


import Task1 as fun


def fib(n):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def negfib(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return negfib(n+2) - negfib(n+1)


num = fun.check_num()


def fib_range(num: int) -> list:
    lst1 = []
    for e in range(0, num + 1):
        lst1.append(fib(e))
    # print(lst1)

    lst2 = []
    for e in range(-num, 0):
        lst2.append(negfib(e))
    # print(lst2)

    lst = lst2 + lst1
    return lst
    # print(lst)


print(fib_range(num))
