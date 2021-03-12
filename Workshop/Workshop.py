from collections.abc import Iterable
class Custom:
    def __init__(self, *args):
        self.values = [el for el in args]

    def append(self, value):
        self.values += [value]

    def remove(self, index):
        try:
            value = self.values[index]
            del self.values[index]
            return value
        except IndexError:
            raise IndexError

    def get(self, index):
        try:
            return self.values[index]
        except IndexError:
            raise IndexError

    def extend(self, itr):
        if isinstance(itr, Iterable):
            [self.append(el) for el in list(itr)]
        return self.values

    def insert(self, idx, val):
        try:
            self.values = self.values[:idx] + [val] + self.values[idx:]
            return self.values
        except IndexError:
            raise IndexError

    def pop(self, idx):
        try:
            value = self.values[idx]
            del self.values[idx]
            return value
        except IndexError:
            raise IndexError

    def clear(self):
        self.values = []

    def index(self, value):

        def index_search(value, itr, count):
            if not itr:
                raise ValueError("No such value in iterable")
            head, *tail = itr
            if head == value:
                return count
            return index_search(value,tail,count+1)
        return index_search(value, self.values, 0)

    def count(self, value):

        def counter(num, itr, count):
            if not itr:
                return count
            head, *tail = itr
            if head == num:
                count += 1
            return counter(num, tail, count)
        return counter(value,self.values,0)

    def reverse(self):
        temp = []
        def reverser(itr,temp):
            if not itr:
                return temp
            head, *tail = itr
            return reverser(tail,[head]+temp)
        return reverser(self.values,temp)

    def copy(self):
        copy = self.values
        return copy


    def size(self):

        def size_check(itr,acc):
            if not itr:
                return acc
            return size_check(itr[1:],acc+1)
        return size_check(self.values,0)

    def add_first(self, value):
        self.values = [value] + self.values

    def dictionize(self):
        keys = [self.values[i] for i in range(len(self.values)) if i % 2 == 0]
        values = [self.values[i] for i in range(len(self.values)) if i % 2 != 0]
        if len(keys) != len(values):
            values.append(" ")
        return {key: value for (key, value) in zip(keys,values)}

    def move(self, amount):
        if amount > self.size():
            raise IndexError
        self.values =  self.values[amount:] + self.values[:amount]
        return self.values


    def sum(self):
        def sum_rec(itr, acc):
            if not itr:
                return acc
            head, *tail = itr
            if not isinstance(head, int):
                head = len(head)
            return sum_rec(tail, acc+head)
        return sum_rec(self.values, 0)


    def overbound(self):
        value = None
        if not self.values:
            raise IndexError("Empty list")
        current = self.values[0] if isinstance(self.values[0],int) else len(self.values[0])
        for el in self.values[1:]:
            if isinstance(el, int):
                if el > current:
                    current = el
                    value = el
            else:
                if len(el) > current:
                    current = len(el)
                    value = el
        return self.index(value)

    def underbound(self):
        value = None
        if not self.values:
            raise IndexError("Empty list")
        current = self.values[0] if isinstance(self.values[0], int) else len(self.values[0])
        for el in self.values[1:]:
            if isinstance(el, int):
                if el < current:
                    current = el
                    value = el
            else:
                if len(el) < current:
                    current = len(el)
                    value = el
        return self.index(value)



a = Custom(1,2,3,4,5,6,7,"AIJSAISJ")
print(a.overbound())