from functools import reduce
import random


class Array:
    '''
    The Array class is a mimic of the python lists, 
    this is design to comprehend the Arrays data 
    structure functionality
    '''
    def __init__(self, capacity, fill_value=None) -> None:
        self.capacity = capacity
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)

    def __getItem__(self, index):
        return self.items[index]

    def __setItem__(self, index, new_item):
        self.items[index] = new_item

    def __randReplace__(self):
        return [self.__setItem__(i, random.randint(0, self.capacity)) for i in range(self.capacity)]

    def __sum__(self):
        return reduce(lambda start, finish: start+finish, self.items)

