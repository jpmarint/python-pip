class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for _ in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item



class StackArray(Array):
    def __init__(self, capacity, fill_value=None):
        super().__init__(capacity, fill_value)
        self.capacity = capacity
        self.top = None
        self.size = 0

    def __str__(self):
        result = ''
        if self.size <= 0:
            return 'Stack empty'
        for i in self.items:
            if i != None:
                result += f'{i} '
        return result

    def push(self, data):
        if self.size == self.capacity:
            print('Stack full')
            return -1

        for i, value in enumerate(self.items):
            if value == None:
                self.items[i] = data
                self.top = data
                self.size += 1
                break

    def pop(self):
        for i in range(self.capacity-1, -1, -1):
            if self.items[i] != None:
                self.items[i] = None
                self.size -= 1
                if i > 0:
                    self.top = self.items[i-1]
                else:
                    self.top = None
                break

    def peek(self):
        if self.top:
            return self.top
        else:
            return "The stack is empty"
    
    def clear(self):
        self.__init__(self.capacity)
    
    def search(self, target_item):
        if self.size <= 0:
            print("The stack is empty")
        else:
            if target_item in self.items:
                print(f'Target item {target_item} has been found')
                return self.items.index(target_item)
            else:
                print(f'Target item {target_item} is not in stack')
                return -1

    def iter(self):
        for element in self.items:
            if element != None:
                yield element