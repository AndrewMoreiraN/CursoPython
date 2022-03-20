from abc import abstractmethod, ABC


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, value):
        self.__agencia = value

    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, value):
        self.__conta = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Saldo precisa ser numérico.')
        self.__saldo = value

    def depositar(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Valor do depósito precisa ser numérico.')

        self.saldo += value
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}', end='\n')

    @abstractmethod
    def sacar(self, value):
        pass
