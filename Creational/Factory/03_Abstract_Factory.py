from abc import ABCMeta, abstractclassmethod


# Factory Abstrata de Grupos
class LocalFactoryAbstrato(metaclass=ABCMeta):
    @abstractclassmethod
    def criar_grupo_sem_healer(cls):
        pass

    @abstractclassmethod
    def criar_com_healer(cls):
        pass


# Factory Concreta de Grupos

class CavernaConcreto(LocalFactoryAbstrato):

    def criar_grupo_sem_healer(self):
        return GuerreiroLadino()

    def criar_com_healer(self):
        return Sacerdote()


class MasmorraConcreto(LocalFactoryAbstrato):

    def criar_grupo_sem_healer(self):
        return MagoBarbaro()

    def criar_com_healer(self):
        return Druida()


#  Produto Abstrato

class SemCura(metaclass=ABCMeta):
    @abstractclassmethod
    def grupo_basico(cls, dungeon):
        pass


class ComCura(metaclass=ABCMeta):
    @abstractclassmethod
    def cura_adicional(cls, dungeon):
        pass


# Produto Concreto referente a Factory GrupoCavernaConcreto

class GuerreiroLadino(SemCura):
    def grupo_basico(self, dungeon):
        print(f"Um Grupo sem cura entrará na {type(dungeon).__name__}, ele é formado por : {type(self).__name__}")


class Sacerdote(ComCura):
    def cura_adicional(self, dungeon):
        print(f"Ao adentrar na {type(dungeon).__name__} vocês receberão a ajuda de um {type(self).__name__}")


# Produto Concreto referente a Factory GrupoMasmorraConcreto


class MagoBarbaro(SemCura):
    def grupo_basico(self, dungeon):
        print(f"Um Grupo sem cura entrará na {type(dungeon).__name__}, ele é formado por : {type(self).__name__}")


class Druida(ComCura):
    def cura_adicional(self, dungeon):
        print(f"Ao adentrar na {type(dungeon).__name__} vocês receberão a ajuda de um {type(self).__name__}")


#  Interface que chamará a Factory específica
class CriarGrupo:

    def __init__(self):
        pass

    def criar_grupos(self):
        for factory in [MasmorraConcreto(), CavernaConcreto()]:
            sem_heal = factory.criar_grupo_sem_healer()
            com_heal = factory.criar_com_healer()
            sem_heal.grupo_basico(factory)
            com_heal.cura_adicional(factory)


if __name__ == "__main__":
    Grupo = CriarGrupo()
    Grupo.criar_grupos()
