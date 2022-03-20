from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, value):
        self.__limite = value

    def sacar(self, value):
        if (self.saldo + self.limite) < value:
            print('Saldo insuficiente')
            return
        self.saldo -= value
        self.detalhes()
