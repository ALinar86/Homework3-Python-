# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

from random import uniform
import Task1 as fun


def list_real_num():
    num = fun.check_num()
    list = []
    for i in range(num):
        list.append(round(uniform(1, 3), 2))
    return list


lst1 = list_real_num()
print(lst1)


def remains_list():
    lst2 = [i % 1 for i in lst1]
    delta =max(lst2) - min(lst2)
    print (delta)

remains_list()
