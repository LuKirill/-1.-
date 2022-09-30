"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

from random import randint


def listf():
    my_list = []
    for i in range(1, 26):
        my_list.append(randint(-15, 15))
    return my_list


# O(n^2)
def min1(lst, min_=None):
    if min_ is None:
        min_ = lst.pop()
    cur = lst.pop()
    if cur < min_:
        min_ = cur
    if lst:
        return min1(lst, min_)
    return min_


print(min1(listf()))


# O(n)
def min2(lst):
    min_ = lst[0]
    for j in lst:
        if j < min_:
            min_ = j
    return min_


print(min2(listf()))
