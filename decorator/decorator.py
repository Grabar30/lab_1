class Man():
    """Human"""
    def __init__(self, name):
        self._name = name

class Jetpack():
    """Реактивный ранец"""
    def __init__(self, man):
        self._man = man

    def fly(self):
        # покаызываем функциональность объекта  возможность летать
        print('{} летит на реактивном ранце!'.format(self._man._name))


man = Man('Виктор')

man_jetpack = Jetpack(man)
man_jetpack.fly()  # Виктор летит на реактивном ранце!
