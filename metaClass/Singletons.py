class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        print(cls, cls._instances)
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            print(super(Singleton, cls))
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):
    pass


class RegularClass():
    pass


x = SingletonClass()
y = SingletonClass()
print(x, y)
print(x == y)
x = RegularClass()
y = RegularClass()
print(x, y)
print(x == y)
