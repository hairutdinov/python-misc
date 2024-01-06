import itertools
from random import random


class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        self.i += 1
        if self.i > self.k:
            raise StopIteration
        return random()

    def __iter__(self):
        return self


# for rand in RandomIterator(2):
#     print(rand)


# class PaginationIterator:
#     def __init__(self, items, page_size: int = 2):
#         self.items = items
#         self.page_size = page_size
#         self.total_items = len(items)
#         self.page_number = 1
#         self.total_pages = (self.total_items + self.page_size - 1) // self.page_size
#
#     def __next__(self):
#         if self.page_number > self.total_pages:
#             raise StopIteration
#         start_index = (self.page_number - 1) * self.page_size
#         end_index = self.page_number * self.page_size
#         self.page_number += 1
#         return self.items[start_index:end_index]


class PaginationIterator:
    def __init__(self, items, page_size: int = 2):
        self.items = items
        self.page_size = page_size

    def __iter__(self):
        it = iter(self.items)
        while batch := tuple(itertools.islice(it, self.page_size)):
            yield batch


class MyList(PaginationIterator, list):
    pass
    # def __iter__(self):
    #     return PaginationIterator(self)


for pair in MyList([1,2,3,4,5,6,7]):
    print(pair)