task1: Поправил сложности в О-нотациях
task2: в первой задаче сложность О(n^2), во второй сложность O(n)
task3: Исправил сложность для for j in dict_().keys(): #  O(n)
task4: Исправил сложность для list_keys = list(log_pass.keys()) #  O(n)
Исправил сложность для if i in list_keys: #  O(n)
task5: добавил метод удаления тарелок из стопки:

def out(self):
    for i in self.elems:
        if len(i) == 1:
            self.elems.pop()
    if len(self.elems) > 0:
        self.elems[-1].pop() 
