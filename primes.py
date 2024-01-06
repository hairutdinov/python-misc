import itertools


def primes():
    number = 1
    while True:
        number += 1
        if all(number % i for i in range(2, int(number ** 0.5) + 1)):
            yield number


print(list(itertools.takewhile(lambda x : x <= 31, primes())))
