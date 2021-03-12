def type_check(type):
    def decorator(func):
        def wrapper(*args):
            if len(args) == len([x for x in args if isinstance(x,type)]):
                result = func(*args)
                return result
            return "Bad Type"
        return wrapper
    return decorator




@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))



@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))
