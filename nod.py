from functools import reduce
import operator
import math
from collections import Counter


def divisors(number):
    return [nod for nod in range(1, number + 1) if number % nod == 0]


def gcd_method_one(*numbers):
    # * Найти делители первого и второго числа
    # * Найти среди них наибольший общий делитель
    return max(set.intersection(*map(lambda num: set(divisors(num)), numbers)))


print(gcd_method_one(12, 9))
print(gcd_method_one(24, 18))
print(gcd_method_one(12, 24, 36, 42))


def is_prime_number(number):
    # Check for factors from 2 to the square root of the number
    # Проверьте множители от 2 до квадратного корня числа
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_prime_number(is_prime_number_cb=None, offset: int = 0):
    """
       Generates prime numbers starting from the given offset.

       Args:
           is_prime_number_cb (callable): A function to check if a number is prime.
                                       Defaults to the built-in is_prime_number function.
           offset (int): The starting point for generating prime numbers.

       Returns:
           generator: A generator function for prime numbers.
       """
    current_number = offset
    is_prime = is_prime_number_cb or is_prime_number

    def generator():
        nonlocal current_number
        while True:
            current_number += 1
            if is_prime(current_number):
                yield current_number

    return generator


def prime_factors(number):
    factors = []
    prime_num_generator = generate_prime_number(offset=1)
    prime_number = next(prime_num_generator())

    while not is_prime_number(number):
        if number % prime_number != 0:
            prime_number = next(prime_num_generator())
            continue

        number = number // prime_number
        factors.append(prime_number)

    return factors + [number]


def list_intersection(*lists):
    # def elements_count(_list):
    #     el_cnt = {}
    #     for el in _list:
    #         el_cnt[el] = el_cnt.get(el, 0) + 1
    #     return el_cnt

    element_count = [Counter(_list) for _list in lists]
    keys_intersection_set = set.intersection(*map(set, element_count))
    intersection = []
    for element in keys_intersection_set:
        intersection.extend([element] * min(map(lambda _list: _list[element], element_count)))
    return intersection
    # return list((Counter(list1) & Counter(list2)).elements())


# print(list_intersection([2, 3, 3], [2, 2, 2, 3], [2, 2, 3, 3]))


def gcd_method_two(*numbers):
    # * Разложить оба числа на простые множители
    # * Перемножить общие их них
    # return reduce(operator.mul, list_intersection(prime_factors(a), prime_factors(b)))
    return math.prod(list_intersection(*map(prime_factors, numbers)))


# print(gcd_method_two(12, 24, 36, 42))

def list_relative_complement(list1, list2):
    """
        Ищет разницу list1 - list2
    """
    return list((Counter(list1) - Counter(list2)).elements())


# print(list_relative_complement([2, 2, 2], [2, 3, 3]))

def gcd_method_three(a, b):
    # * Разложить оба числа на простые множители
    # * Из разложения первого числа вычеркнуть числа,
    # которые не входят в разложение второго числа
    # * Оставшиеся числа в первом разложении переумножить
    pass


def gcd_euclidean_algorithm(*numbers: int):
    """
        Greatest Common Divisor - The Euclidean Algorithm
        1. Большее число поделить на меньшее
        2. Если остаток не равен 0, то меньшее число поделить на остаток
        3. Если остаток не равен 0, первый остаток поделить на второй остаток
        4. Деление продолжается пока в остатке не будет 0. Последний делитель и есть НОД.
    """
    numbers = list(numbers)
    gcd_result = None

    while len(numbers) > 1:
        a, b = numbers.pop(), numbers.pop()
        lesser_num, greater_num = min(a, b), max(a, b)

        while lesser_num:
            greater_num, lesser_num = lesser_num, divmod(greater_num, lesser_num)[1]

        numbers.append(greater_num)
        gcd_result = greater_num

    return gcd_result

nums = [140, 96, 92]
print("gcd(%s)" % (",".join(map(str, nums))), gcd_euclidean_algorithm(*nums))
