class Estalajadeiro:

    def __init__(self):
        print("-------------------------------------------------------")
        print("Estalajadeiro: Vou verificar se temos tudo, um segundo.")
        print("-------------------------------------------------------")

    def trabalhando(self):
        self.Camareira = Camareira()
        self.Camareira.prepara_quarto()

        self.cozinheiro = Cozinheiro()
        self.cozinheiro.preparando_comida()

        self.adega = Adega()
        self.adega.pegando_bebida()


class Camareira:
    def __init__(self):
        print("Camareira: 'Verificando quartos...")

    def __verifica_vaga(self):
        print("Camareira: O quarto está vago!")
        return True

    def prepara_quarto(self):
        if self.__verifica_vaga():
            print("Camareira: Inicia a limpeza do quarto.")


class Cozinheiro:
    def __init__(self):
        print("Cozinheiro: Estou acendendo o fogo!")

    def preparando_comida(self):
        print("Cozinheiro:'Wild pie está sendo preparada.' ")


class Adega:
    def __init__(self):
        print("Adega: 'Procurando a bebida...'")
        self.hidromel = True

    def pegando_bebida(self):
        if self.hidromel:
            print("Adega: 'Retorna Hidromel.'")


class Aventureiro:
    def __init__(self):
        print("-------------------------------------------------------")
        print("'O aventureiro adentra a estalagem....'")

    def fazer_pedido(self):
        print("Aventureiro: Olá estalajadeiro, eu gostaria de um Hidromel, uma Wild pie e um quarto para pernoitar.")
        estalajadeiro = Estalajadeiro()
        estalajadeiro.trabalhando()

    def __del__(self):
        print("-------------------------------------------------------")
        print("Aventureiro: Obrigado pelo serviço!")
        print("-------------------------------------------------------")


voce = Aventureiro()
voce.fazer_pedido()
