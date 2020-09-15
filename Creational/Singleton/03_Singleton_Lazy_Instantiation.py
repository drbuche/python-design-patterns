class SingletonLazyInstantiation:

    __instancia = None

    def __init__(self):
        if not SingletonLazyInstantiation.__instancia:
            print('Você chamou o método init')
        else:
            print('O objeto já foi criado!', self.get_instancia())

    @classmethod
    def get_instancia(cls):
        if not cls.__instancia:
            cls.__instancia = SingletonLazyInstantiation()
        return cls.__instancia


obj1 = SingletonLazyInstantiation()  # Você chamou o método init, mas o objeto não foi criado
obj2 = SingletonLazyInstantiation()  # Você chamou o método init, mas o objeto não foi criado
print(obj1)  # <__main__.SingletonLazyInstantiation object at 0x7f2e9f9573d0>
print(obj2)  # <__main__.SingletonLazyInstantiation object at 0x7f2e9f957410>

obj1 = SingletonLazyInstantiation.get_instancia()  # Objeto criado <__main__.SingletonLazyInstantiation object at 0x7f2e9f957550>
obj2 = SingletonLazyInstantiation()  # O objeto já foi criado! <__main__.SingletonLazyInstantiation object at 0x7f2e9f957550>
obj2 = SingletonLazyInstantiation.get_instancia()  # Nova referência para o objeto criado anteriormente.
print(obj1)  # <__main__.SingletonLazyInstantiation object at 0x7f2e9f957550>
print(obj2)  # <__main__.SingletonLazyInstantiation object at 0x7f2e9f957550>
