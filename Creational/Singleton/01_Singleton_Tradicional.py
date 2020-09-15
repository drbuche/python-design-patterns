class SingletonTradicional:
    def __new__(cls):
        if not hasattr(cls, 'instancia'):
            cls.instancia = super(SingletonTradicional, cls).__new__(cls)
        return cls.instancia


b1 = SingletonTradicional()
print(b1)  # <__main__.SingletonTradicional object at 0x7fdd31a1f350>
b2 = SingletonTradicional()
print(b1)  # <__main__.SingletonTradicional object at 0x7fdd31a1f350>
print(b2)  # <__main__.SingletonTradicional object at 0x7fdd31a1f350>
