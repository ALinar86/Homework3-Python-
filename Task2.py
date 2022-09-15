# 2-Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# import Task1 as from_task1

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


# def multiplication(list1: list) -> list:
#     list_new = [list1[i]*list1[-1-i] for i in range(len(list1)//2)]
#     if len(list1) % 2 != 0:
#         middle_index = ((len(list1) - 1) // 2)
#         list_new.append((list1[middle_index]) ** 2)
#     return list_new


def multiplication(list1: list) -> list:
    list_new =[]
    for i in range(len(list1)//2):
        list_new.append(list1[i]*list1[-1-i])
    if len(list1) % 2 != 0:
        middle_index = ((len(list1) - 1) // 2)
        list_new.append((list1[middle_index]) ** 2)
    return list_new


lst = get_list()
print(lst)
# print(len(lst))
lst_new = multiplication(lst)
print(lst_new)
