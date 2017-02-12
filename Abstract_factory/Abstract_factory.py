class furniture:
    def __init__(self):
        self.size = 0

class chair(furniture):
    def __init__(self):
        super().__init__()
        self.size = 0.5

class table(furniture):
    def __init__(self):
        super().__init__()
        self.size = 1.5

def new_furniture():
    "furniture fuctory"
    answer = input("select new type of furniture")
    if answer == "ch":
        return chair()
    elif answer == "tb":
        return table()
    else:
        return None


res = []
while 1:
    obj = new_furniture()
    if obj is None:
        break
    res.append(obj)

print("flat ", res)