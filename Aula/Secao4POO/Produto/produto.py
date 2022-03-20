class Produto:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    # Getter
    @property
    def valor(self):
        if isinstance(self.__valor, str):
            self.__valor = float(self.__valor.replace('R$', ''))
        return self.__valor

    # Setter
    @valor.setter
    def valor(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor.title()

    def desconto(self, percentual):
        self.valor -= (self.valor * (percentual / 100))
