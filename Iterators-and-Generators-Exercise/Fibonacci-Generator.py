def fibonacci():
    fibbo = []
    while True:
        if not fibbo:
            yield 0
            fibbo.append(0)
        elif len(fibbo) == 1:
            yield 1
            fibbo.append(1)
        else:
            yield fibbo[len(fibbo)-2] + fibbo[len(fibbo)-1]
            fibbo.append(fibbo[len(fibbo)-2] + fibbo[len(fibbo)-1])

generator = fibonacci()
for i in range(5):
    print(next(generator))
