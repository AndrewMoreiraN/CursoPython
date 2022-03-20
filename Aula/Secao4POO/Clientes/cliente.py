from endereco import Endereco
from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.__enderecos = []

    @property
    def enderecos(self):
        return self.__enderecos

    @enderecos.setter
    def enderecos(self, endereco):
        self.__enderecos = endereco

    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def falar(self):
        print('Estou em Cliente')
    # def __del__(self):
    #    print(f'{self.nome} foi apagado')
