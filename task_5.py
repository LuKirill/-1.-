"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class StackPlates:
    def __init__(self, a):
        self.elems = []
        self.a = a

    def push(self, el, el_):
        if len(self.elems) == 0:
            self.elems.append([str(el_)])
            el = el - 1
        for i in range(1, el + 1):
            elem = self.elems.pop()
            if len(list(elem)) == self.a:
                self.elems.append(elem)
                self.elems.append([str(el_)])
            if len(list(elem)) < self.a:
                elem.append(str(el_))
                self.elems.append(elem)

    def out(self):
        for i in self.elems:
            if len(i) == 1:
                self.elems.pop()
        if len(self.elems) > 0:
            self.elems[-1].pop()


b = StackPlates(5)
b.push(6, "qwert")
b.push(3, 'dfb')
b.push(4, 1)
b.out()
b.out()
b.out()
print(b.elems)
