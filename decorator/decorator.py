

def make(f):
    print("on init")
    def make_some_work():
        print("befor")
        f()
        print("after")
    return make_some_work

@make
def say():
    print("Hello people")

@make
def say1():
    print("Hello people1")
print("-----------------------")

say()
say1()
