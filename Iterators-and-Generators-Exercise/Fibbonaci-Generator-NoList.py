def fibonacci():
    previous = 0
    current = 1
    while True:
        yield previous
        previous, current = current, previous+current

generator = fibonacci()
for i in range(5):
    print(next(generator))
