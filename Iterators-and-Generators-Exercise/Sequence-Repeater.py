class sequence_repeat:
    def __init__(self, string, count):
        self.string = string
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            self.index += 1
            if self.index >= len(self.string):
                self.index = 0
            self.count -= 1
            return self.string[self.index-1]
        raise StopIteration()

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
