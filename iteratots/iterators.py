class iterators:
    def __init__(self, lst=[]):
        self.list = lst
        self.index = -1
        self.last_index = len(self.list) - 1

    def next(self):
        self.index += 1
        return self.index <= self.last_index

    def current(self):
        return self.list[self.index]

class Tit:

    def __init__(self, li):
        self.li = li
        self.count = 0

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        self.count += 1
        return self.li[self.count-1]



a = [2,3,[4,5]]

# for i in Tit(a):
#     print(i)

b = iterators(a)

while b.next():
    print(b.current())

