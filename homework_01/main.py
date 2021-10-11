"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    [1, 4, 25, 49]
    """
    square = []
    for num in args:
        square.append(num ** 2)
    return square


def is_prime(*args) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список простых чисел
    """
    primes = []
    for num in args:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, numbers_type) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    [2, 4]
    """

    if numbers_type == "odd":  # Не четные числа
        return list(filter(lambda num: num % 2 != 0, numbers))
    elif numbers_type == "even":  # Четные числа
        return list(filter(lambda num: num % 2 == 0, numbers))
    elif numbers_type == "prime":  # Простые числа
        return list(filter(is_prime, numbers))
    else:
        print("Что-то пошло не так!")
        return numbers


# print("Не четные числа:", filter_numbers(range(1, 20), ODD))
# print("Четные числа:", filter_numbers(range(1, 20), EVEN))
# print("Простые числа:", filter_numbers(range(1, 20), PRIME))
# filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 555)
