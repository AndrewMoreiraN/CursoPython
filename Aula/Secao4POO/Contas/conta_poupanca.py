from conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, value):
        if self.saldo < value:
            print('Saldo insuficiente')
            return
        self.saldo -= value
        self.detalhes()
