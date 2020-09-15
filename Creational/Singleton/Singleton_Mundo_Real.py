class CheckSanidade:

    __instancia = None

    def __new__(cls, *args, **kwargs):
        if not CheckSanidade.__instancia:
            CheckSanidade.__instancia = super(CheckSanidade, cls).__new__(cls, *args, **kwargs)
        return CheckSanidade.__instancia

    def __init__(self):
        self._servidores = []

    def add_servidor(self):
        self._servidores.append("Server 1")
        self._servidores.append("Server 2")
        self._servidores.append("Server 3")
        self._servidores.append("Server 4")

    def mudar_servidores(self):
        self._servidores.pop()
        self._servidores.append("Novo Server 5")


obj1 = CheckSanidade()
print(obj1)  # <__main__.CheckSanidade object at 0x7f01bbf58710>
obj2 = CheckSanidade()
print(obj2)  # <__main__.CheckSanidade object at 0x7f01bbf58710>

# O obj1 e obj2 são referências diferentes ao mesmo objeto at 0x7f01bbf58710.

obj1.add_servidor()
print(obj1._servidores)  # ['Server 1', 'Server 2', 'Server 3', 'Server 4']
print(obj2._servidores)  # ['Server 1', 'Server 2', 'Server 3', 'Server 4']

obj2.mudar_servidores()

print(obj1._servidores)  # ['Server 1', 'Server 2', 'Server 3', 'Novo Server 5']
print(obj2._servidores)  # ['Server 1', 'Server 2', 'Server 3', 'Novo Server 5']
