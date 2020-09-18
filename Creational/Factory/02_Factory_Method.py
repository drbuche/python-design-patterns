from abc import ABC, abstractclassmethod  # Módulos que possibilitam a criação de uma classe abstrata.

"""
 V - Implementação da clase abstrata 'Product'. - V
 
"""


class Armamento(ABC):
    @abstractclassmethod  # Método abstrato genérico que sera herdado.
    def arma(cls):
        pass


"""
 V - Varias clases 'ConcreteProduct'. - V

"""


class Machado(Armamento):
    def arma(self):  # Real implementação do método arma, de acordo com a característica de cada classe.
        print("Machado de Ferro")


class Espada(Armamento):
    def arma(self):
        print("Espada Longa")


class Arco(Armamento):
    def arma(self):
        print("Arco de Madeira")


class Escudo(Armamento):
    def arma(self):
        print("Escudo de Ferro")


class Flecha(Armamento):
    def arma(self):
        print("Flecha de Mithril")


class Adaga(Armamento):
    def arma(self):
        print("Damascus")




"""
 V - Classe abstrata 'Creator'. - V

"""


class Personagem(ABC):
    def __init__(self):
        self.equipamentos = []
        self.criar_personagem()

    @abstractclassmethod
    def criar_personagem(cls):  # Método abstrato para criar perfil.
        pass

    def get_nome_das_armas(self):  # Método para retornamos nossa lista de equipamentos.
        return self.equipamentos

    def adicionar_arma(self, arma):  # Método que recebe as 'armas' que devem ser adicionadas na lista 'equipamentos'
        self.equipamentos.append(arma)


"""
 V - Classes concretas para criação do objeto 'ConcreteClass'. - V

"""


class Arqueiro(Personagem):

    def criar_personagem(self):  # Método que realmente cria a instância.
        self.adicionar_arma(Arco())
        self.adicionar_arma(Flecha())
        self.adicionar_arma(Adaga())


class Guerreiro(Personagem):

    def criar_personagem(self):  # Método que realmente cria a instância.
        self.adicionar_arma(Espada())
        self.adicionar_arma(Escudo())
        self.adicionar_arma(Adaga())


class Barbaro(Personagem):

    def criar_personagem(self):  # Método que realmente cria a instância.
        self.adicionar_arma(Machado())
        self.adicionar_arma(Escudo())



qual_personagem = input("Qual sua classe?")  # Arqueiro
personagem = eval(qual_personagem)()  # Objeto criado
print(f"Criando o personagem {type(personagem)}")  # Criando o personagem Arqueiro
print(f"Personagem criado com sucesso! {personagem.get_nome_das_armas()}")  # Personagem criado com sucesso! [<__main__.Arco object at 0x7fdb1e1801d0>, <__main__.Flecha object at 0x7fdb1e180210>, <__main__.Adaga object at 0x7fdb1e180250>]









