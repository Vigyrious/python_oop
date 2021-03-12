class Calculator:
    @staticmethod
    def add(*args):
        return sum([i for i in args])

    @staticmethod
    def multiply(*args):
        curr = 1
        for i in args:
            curr *= i
        return curr

    @staticmethod
    def divide(*args):
        curr = args[0]
        for i in range(1,len(args)):
            curr /= args[i]
        return curr

    @staticmethod
    def subtract(*args):
        curr = args[0]
        for i in range(1, len(args)):
            curr -= args[i]
        return curr


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
