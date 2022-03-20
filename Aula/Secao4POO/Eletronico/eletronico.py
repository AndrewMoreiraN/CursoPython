class Eletronico:
    def __init__(self, nome):
        self.__nome = nome
        self.__ligado = False

    def ligar(self):
        if self.ligado:
            return
        self.ligado = True

    def desligar(self):
        if not self.ligado:
            return
        self.ligado = True

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def ligado(self):
        return self.__ligado

    @ligado.setter
    def ligado(self, value):
        self.__ligado = value

    @ligado.deleter
    def ligado(self):
        pass
