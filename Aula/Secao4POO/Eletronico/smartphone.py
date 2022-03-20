from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self.__conectado = False

    @property
    def conectado(self):
        return self.__conectado

    @conectado.setter
    def conectado(self, value):
        self.__conectado = value

    def conectar(self):
        if not self.ligado:
            error = f'{self.nome} não esta ligado.'
            self.log_error(error)
            return

        if self.conectado:
            error = f'{self.nome} já está conectado. '
            self.log_error(error)
            return

        self.conectado = True
        info = f'{self.nome} está conectado'
        self.log_info(info)

    def desconectar(self):
        if not self.conectado:
            error = f'{self.nome} não está conectado'
            self.log_error(error)
            return

        self.conectado = False
        info = f'{self.nome} está desconectado'
        self.log_info(info)
