class MonostateBorg:

    __compartilhado = {"1": "2"}

    def __init__(self):
        self.__dict__ = self.__compartilhado
        pass


obj1 = MonostateBorg()
print(obj1)  # <__main__.MonostateBorg object at 0x7f43aea40590>
obj2 = MonostateBorg()
print(obj1)  # <__main__.MonostateBorg object at 0x7f43aea40590>
print(obj2)  # <__main__.MonostateBorg object at 0x7f43aea4f510>
print(obj1.__dict__)  # {'1': '2'}
print(obj2.__dict__)  # {'1': '2'}
obj2.novo_dado = 5
print(obj1.__dict__)  # {'1': '2', 'novo_dado': 5}
print(obj2.__dict__)  # {'1': '2', 'novo_dado': 5}

