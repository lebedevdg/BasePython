# def funk(test):

#     sieve = [True] * test
#     for i in range(2, test):
#         if sieve[i]:
#             print(i)
#             for j in range(i*1, test, i):
#                 sieve[j] = False


# funk(10000000)


import builtins


class BaseProd:
    type_name = None

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} ({self.type_name})'

    def __add__(self, other):
        return self.price + other.price

    def make_discount(self, discount):
        self.price *= (100 - discount) / 100


class Phone(BaseProd):
    type_name = 'Телефон'


class NoteBook(BaseProd):
    type_name = 'Ноутбук'


product_1 = Phone('iphone', 440000000000000000000000000000000000000000)
product_2 = NoteBook('makebook', 34000)

basket = product_1 + product_2
print(basket)

print("Hello World")


dfsdf
