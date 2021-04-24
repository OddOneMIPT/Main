class Knot():

    def __init__(self, knot = None):
        self.knot = knot
        self.next_knot = None
        self.prev_knot = None



class List():

    #Определяем функцию внутри класса
    @staticmethod
    def my_range(start, finish = None, step = 1):
        if finish is None:
            start, finish = 0, start
        current = start
        while current + step <= finish:
            yield current
            current += step

    #инициализация простая, просто создаём объект нашего класса
    def __init__(self):
        self.start = None
        self.length = 0

    #Чтобы добавить узел реализуем следующую штуку
    def addKnotToEnd(self, new_value):
        new_knot = Knot(new_value)
        self.length += 1
        if self.start is None:
            self.start = new_knot
            return
        last_knot = self.start
        while (last_knot.next_knot):
            last_knot = last_knot.next_knot
        last_knot.next_knot = new_knot
        new_knot.prev_knot = last_knot

    #после того, как мы научились добавлять элемент, давайте искать 
    def contains_value(self, value):
        last_knot = self.start
        while(last_knot):
            if value == last_knot.knot:
                return True
            else:
                last_knot = last_knot.next_knot
        return False

    #Поиск элемента по индекц
    def get_by_index(self, index):
        last_knot = self.start
        knot_index = 0
        while knot_index <= index:
            if knot_index == index:
                return last_knot.knot
            knot_index += 1
            last_knot = last_knot.next_knot
            if last_knot.next_knot == None:
                print('Элемента с таким номером нет, в списке всего ', index, ' элементов')
                return

    #Добавить элемент по индексу
    def add_by_index(self, value, index):
        knot_index = 0
        self.length += 1
        last_knot = self.start
        new_knot = Knot(value)
        if not index:
            self.add_to_start(value)
            return
        while (last_knot):
            if knot_index == index:
                left_knot = last_knot.prev_knot
                right_knot = last_knot
                left_knot.next_knot = new_knot
                new_knot.prev_knot = left_knot
                new_knot.next_knot = right_knot
                right_knot.prev_knot = new_knot
                return
            else:
                knot_index += 1
                last_knot = last_knot.next_knot     
        else:
            self.addKnotToEnd(value)

    #Добавить в начало
    def add_to_start(self, value):
        new_knot = Knot(value)
        if self.start is None:
            self.addKnotToEnd(value)
            return
        else:
            self.start.prev_knot = new_knot
            new_knot.next_knot = self.start
            self.start = new_knot
            self.length += 1
            return

    #Убрать узел по значению
    def remove_knot(self, rvalue):
        start = self.start

        if start is not None:
            if start.knot == rvalue:
                self.start = start.next_knot
                self.start.prev_knot = None
                start = None
                self.length -= 1
                return
            while start is not None:
                if start.knot == rvalue:
                    break
                last_knot = start
                start = start.next_knot
            if start == None:
                print("Такого элемента нет")
                return
            last_knot.next_knot = start.next_knot
            start.next_knot.prev_knot = None
            start = None
            self.length -= 1


    #Убрать по индексу
    def remove_knot_by_index(self,index):
        last_knot = self.start
        knot_index = 0
        if self.length == 0:
            print("Пустой List")
            return
        while last_knot:
            if knot_index == index:
                left_knot = last_knot.prev_knot
                right_knot = last_knot.next_knot
                if not left_knot and not right_knot:
                    left_knot.next_knot = right_knot
                    right_knot.prev_knot = left_knot
                    self.length -= 1
                    return
                if not left_knot:
                    right_knot.prev_knot = None
                    self.start = right_knot
                    self.length -= 1
                    return
                if not  right_knot:
                    left_knot.next_knot = None
                    self.length = -1
                    return
            knot_index += 1
            last_knot = last_knot.next_knot
        else:
            print("До такого индекса мы не добрались")
                
    #Печать всего списка
    def Lprint(self):
        current_knot = self.start
        print("List")
        print('-----')
        i = 0
        while current_knot is not None:
            print(str(i) + ':' + str(current_knot.knot))
            current_knot = current_knot.next_knot
            i += 1
        print("-----")

    #Итерация по элементам
    def __iter__(self):
        self.__curr = self.start
        return self

    def __next__(self):
        if self.__curr is None:
            raise StopIteration()
        value = self.__curr.knot
        self.__curr = self.__curr.next_knot
        return value

    #Сортировка тупым пузырьком
    def sort(self, revers = 0):
        if revers == 0:
            for _ in List.my_range(self.length-1):
                start = self.start
                for __ in List.my_range(self.length-1):
                    if start.knot > start.next_knot.knot:
                        start.knot, start.next_knot.knot = start.next_knot.knot, start.knot
                    start = start.next_knot
        else:
            for _ in List.my_range(self.length-1):
                start = self.start
                for __ in List.my_range(self.length-1):
                    if start.knot < start.next_knot.knot:
                        start.knot, start.next_knot.knot = start.next_knot.knot, start.knot
                    start = start.next_knot

    @staticmethod
    def linar(number, stop = 1, start = 0):
        step = (stop - start) / number
        arr = List()
        for i in List.my_range(number+1):
            arr.addKnotToEnd(round(start+step*i, 2))
        return arr



#Генератор чисел фиброначи от 0 до N

def fibonachi(N):
    fib = List.linar(1)
    current_fib = fib.get_by_index(0)
    if N == 0:
        raise IndexError
    for i in List.my_range(N):
        yield i + 1, int(current_fib)
        next_fib = fib.start.knot + fib.start.next_knot.knot
        fib.start.knot = fib.start.next_knot.knot
        fib.start.next_knot.knot = next_fib
        current_fib = fib.start.knot

sep = "-----"
fib = fibonachi(4)
print(next(fib))
next(fib)
next(fib)
print(next(fib))
print(sep)
for i in fibonachi(10):
    print(i)






        
        
        


           
            
"""





Хочу реализовать следующие функции:



knot = List.lina(3)

print(2)
knot.sort()
print(knot.start.knot)
knot.Lprint()
knot.sort(revers=1)
knot.Lprint()

#        for i in knot:
 #           print(i)
"""