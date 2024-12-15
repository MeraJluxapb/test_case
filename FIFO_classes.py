from collections import deque


# реализация с помощью списка
class Buffer:

    def __init__(self, max_length):
        self.max_length = max_length
        self.lst = [None] * self.max_length
        self.length = 0
        self.tail = 0
        self.head = 0

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.max_length

    def put(self, value):
        if self.is_full():
            raise Exception("Buffer is full")
        self.lst[self.tail] = value
        self.tail = (self.tail + 1) % self.max_length
        self.length += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Buffer is empty")
        res = self.lst[self.head]
        self.lst[self.head] = None
        self.head = (self.head + 1) % self.max_length
        self.length -= 1
        return res


# и с помощью встроенной деки
class Buffer_:

    def __init__(self, max_length):
        self.max_length = max_length
        self.lst = deque()

    def is_empty(self):
        return len(self.lst) == 0

    def is_full(self):
        return len(self.lst) == self.max_length

    def push(self, value):
        if self.is_full():
            raise Exception("Buffer is full")
        self.lst.append(value)

    def pop(self):
        if self.is_empty():
            raise Exception("Buffer is empty")
        return self.lst.popleft()