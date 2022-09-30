"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

log_pass = {
    "login1": ("password1", 1),
    "login2": ("password2", 1),
    "login3": ("password3", 1),
    "login4": ("password4", 1),
    "login5": ("password5", 1)
}


def repeat():
    while True:
        f = input('repeat?\n')
        if f == 'yes':
            authentication1()
        elif f == 'no':
            print("Chao!")
            exit()
        else:
            print("Choose "'yes'" or "'no'"")


#########################################################
def login(key):
    list_keys = list(log_pass.keys())  # O(1)
    if key in list_keys:  # O(n)
        return key  # O(1)


def authentication1():
    user_log = input("input login: ")  # O(1)
    if user_log == login(user_log):  # O(1)
        print()
    else:
        print("wrong login")
        repeat()
    user_pass = input("input password: ")  # O(1)
    if log_pass[login(user_log)][0] == user_pass:  # O(1)
        print("enter the system")
    else:
        print("wrong password")
        repeat()
    user_aut = input("press 1 to confirm login ")  # O(1)
    if str(log_pass[login(user_log)][1]) == user_aut:  # O(1)
        print("authentication passed")
    else:
        print("authentication failed")
        repeat()


authentication1()


# итоговая сложность O(n)
###################################################
def authentication2():
    def log(key):
        list_keys = list(log_pass.keys())  # O(1)
        for i in list_keys:  # O(n)
            if i in list_keys:  # O(n**2)
                return key  # O(1)

    user_log = input("input login: ")  # O(1)
    if user_log == log(user_log):  # O(1)
        print()
    else:
        print("wrong login, go to authentication")
        exit()
    user_pass = input("input password: ")  # O(1)
    if log_pass[login(user_log)][0] == user_pass:  # O(1)
        print("enter the system")
    else:
        print("wrong password")
        repeat()
    user_aut = input("press 1 to confirm login ")  # O(1)
    if str(log_pass[login(user_log)][1]) == user_aut:  # O(1)
        print("authentication passed")
    else:
        print("authentication failed")
        repeat()


authentication2()
# итоговая сложность O(n**2)
##################################################################
# сложность примера 1 ниже сложности примера 2, т.к. О(n**2) сложнее O(n)