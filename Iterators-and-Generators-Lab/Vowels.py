class vowels:
    def __init__(self, data):
        self.data = data
        self.counter = 0
    def __iter__(self):
        return self

    def __next__(self):
        temp = self.counter
        self.counter += 1
        if self.counter <= len(self.data):
            if self.data[temp].lower() in "aeoyui":
                return self.data[temp]
            return self.__next__()
        raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
