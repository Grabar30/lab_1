class Man():
    def __init__(self, name):
        self._name = name

class make():
    def __init__(self, man):
        self._man = man

    def say(self):
        # shows the functionality of the object to say
        print('{} , say hi'.format(self._man._name))


man = Man("Niko")

man_make = make(man)
man_make.say()
