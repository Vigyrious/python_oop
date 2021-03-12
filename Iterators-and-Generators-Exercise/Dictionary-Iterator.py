class dictionary_iter:

    def __init__(self, data):
        self.data = data
        self.length = len(self.data)
        self.counter = 0
        self.keys = list(self.data.keys())
    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.length:
            key = self.keys[self.counter]
            value = self.data[key]
            self.counter += 1
            return (key, value)
        raise StopIteration()
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
