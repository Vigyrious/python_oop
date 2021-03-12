class countdown_iterator:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.start
        self.start -= 1
        if self.start >= -1:
            return temp
        raise StopIteration()


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
