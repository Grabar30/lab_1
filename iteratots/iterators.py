class iterators:
    "implementation of the iterators"
    def __init__(self, lst=[]):
        self.list = lst
        self.index = -1
        self.last_index = len(self.list) - 1

    def next(self):
        "go to next element"
        self.index += 1
        return self.index <= self.last_index

    def current(self):
        return self.list[self.index]


a = [2, 3, [4, 5]]

b = iterators(a)

while b.next():
    print(b.current())

