def get_primes(data):
    for num in data:
        if num == 2:
            yield 2
        elif num < 2:
            continue
        else:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
            if is_prime:
                yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))