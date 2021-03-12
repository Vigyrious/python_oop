def even_numbers(function):
    def wrapper(*args, **kwargs):
        numbers = function(*args, **kwargs)
        return [int(i) for i in numbers if i % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))
