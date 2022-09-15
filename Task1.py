# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint


def check_num():
    try:
        num = int(input("Enter number: "))
        return num
    except ValueError:
        print('Error')
        return check_num()


def get_list():
    num = check_num()
    list1 = [randint(-9, 9) for i in range(num)]
    return list1


# print(get_list())


def sum_odd_number(list1: list) -> int:
    sum = 0
    for i in range(len(list1)):
        if i % 2 != 0:
            sum += list1[i]
    return sum

lst = get_list() 
print(lst)
sum_odd = sum_odd_number(lst)
print(sum_odd)
