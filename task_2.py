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

my_list = [4, 4, 6, -2, 5, 7, -45, 65]


# O(n^2)
def min_1(lst):
    my_lst = lst  # O(1)
    for i in lst:  # O(n)
        my_list = []  # O(1)
        for j in my_lst:  # O(n^2)
            if j < i:  # O(1)
                my_list.append(j)  # O(1)
        if len(my_list) == 1:  # O(1)
            return my_list[0]  # O(1)
        my_lst = my_list  # O(1)


print(min_1(my_list))


# O(n)
def min2(lst):
    min_ = lst[0]  # O(1)
    for j in lst:  # O(n)
        if j < min_:  # O(1)
            min_ = j  # O(1)
    return min_  # O(1)


print(min2(my_list))
