"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие нескольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
from random import randint


class DeskClass:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.queue3 = []

    def to_queue1(self, item):
        self.queue1.insert(0, item)

    def out_queue1(self):
        return self.queue1.pop()

    def to_queue2(self):
        a = self.queue1.pop()
        self.queue2.insert(0, a)

    def out_queue2(self):
        return self.queue2.pop()

    def to_queue3(self):
        print(f'Введите 1, чтобы выбрать из какого списка прилетит задача')
        while True:
            k = input('> ')
            if k == "1":
                k = str(k)
                if k == "1":
                    k = randint(0, 1)
                if k == 0:
                    a = self.queue1.pop()
                    self.queue3.insert(0, a)
                elif k == 1:
                    b = self.queue2.pop()
                    self.queue3.insert(0, b)
                break
            else:
                print(f'Вы ввели недопустимый символ. Введите 1')
        return k


if __name__ == '__main__':
    DC = DeskClass()

    # помещаем объекты в очередь
    DC.to_queue1('qwe')
    DC.to_queue1(7)
    DC.to_queue1('asd')
    DC.to_queue1('zxc')
    DC.to_queue1(9.4)
    DC.to_queue2()
    DC.to_queue2()
    # DC.to_queue3()
    DC.to_queue3()
    # получаем очередь
    print(DC.queue1)
    print(DC.queue2)
    print(DC.queue3)
    print()
