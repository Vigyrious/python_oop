def vowel_filter(function):

    def wrapper():
        result = function()
        return [i for i in result if i.lower() in "aeouiy"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
