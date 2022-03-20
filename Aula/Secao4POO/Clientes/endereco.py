class Endereco:
    def __init__(self, cidade, estado):
        self.__cidade = cidade
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade

    @property
    def estado(self):
        return self.__estado

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    # def __del__(self):
    #    print(f'{self.__estado} foi apagado')
