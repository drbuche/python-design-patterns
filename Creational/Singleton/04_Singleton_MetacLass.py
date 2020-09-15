class SingletonMetaCLass(type):  # Type: Possibilita o método __call__

    __instancia = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instancia:
            print('Instancia criada!')
            cls.__instancia[cls] = super(SingletonMetaCLass, cls).__call__(*args, **kwargs)
        else:
            print('Objeto já instanciado')
        return cls.__instancia[cls]


class Controlada(metaclass=SingletonMetaCLass):
    pass


obj1 = Controlada()  # Instancia criada!
print(obj1)  # <__main__.Controlada object at 0x7fdc21ca8590>
obj2 = Controlada()  # Objeto já instanciado
print(obj2)  # <__main__.Controlada object at 0x7fdc21ca8590>

