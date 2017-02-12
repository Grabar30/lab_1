from singletone import a
print(a)


def singleton(cls):
    instances = {}
    def getinstance():
        print("inst", instances)
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class myClass:
    pass

@singleton
class myClass1:
    pass

obj1 = myClass()
obj2 = myClass()
print(obj1 is obj2)

obj1 = myClass1()
obj2 = myClass1()
print(obj1 is obj2)
