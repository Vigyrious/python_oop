from itertools import permutations

def possible_permutations(data):
    for perm in permutations(data):
        yield list(perm)

[print(n) for n in possible_permutations([1, 2, 3])]