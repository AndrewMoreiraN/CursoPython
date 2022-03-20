from account import Account


class ContaCorrente(Account):
    def __init__(self, agency, number, balance, limite=100):
        super().__init__(agency, number, balance)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, value):
        self.__limite = value

    def withdraw(self, value):
        if value > self.balance + self.limite:
            print(f'{value} é maior que o permitido.')
            return
        self.balance -= value
        self.details()
