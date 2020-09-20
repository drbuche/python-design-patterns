from abc import ABCMeta, abstractmethod  # Módulos que possibilitam a criação de uma classe abstrata.


class Sociedade(metaclass=ABCMeta):  # Implementação da classe abstrata.
    @abstractmethod  # Implementação do método abstrato.
    def fala(self):
        pass


class Aragorn(Sociedade):
    def fala(self):  # Polimorfismo.
        print("Minha espada é sua!")


class Legolas(Sociedade):
    def fala(self):  # Polimorfismo.
        print("E o meu arco é seu!")


class Gimili(Sociedade):
    def fala(self):  # Polimorfismo.
        print("E meu machado!")


class FabricaDeFalas:
    @staticmethod
    def crie_fala(class_do_personagem):  # Método que será chamado para criar o objeto.
        '''
        :param class_do_personagem: O termo 'eval' é responsável por pegar a string de um input e lê-lo como uma variável.
        :return: retorna o nome do personagem+ ()+ .fala() -> ex: Gimili().fala()
        '''
        return eval(class_do_personagem)().fala()


# obj1 = Sociedade()  # Erro, pois não podemos criar um objeto utilizando uma classe abstrata!

fdf = FabricaDeFalas
personagem = input('Quem fala o que?')  # Gimili
fdf.crie_fala(personagem)  # E meu machado!

