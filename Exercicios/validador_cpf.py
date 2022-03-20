import re
from random import randint


class ValidadorCPF:
    def __init__(self):
        self.cpf = '000000000'
        self.cpf_tem = '000000000'

    @staticmethod
    def conta_cpf(soma):
        return '0' if 11 - soma % 11 > 9 else str(11 - soma % 11)

    def recebe_cpf(self, cpf):
        cpf = re.sub(r'[^0-9]', '', cpf)
        self.cpf = cpf
        if len(self.cpf) > 9:
            self.cpf_tem = self.cpf[0:9]
        else:
            self.cpf_tem = self.cpf
        return cpf

    def gera_cpf(self):
        self.cpf_tem = str(randint(100000000, 999999999))
        self.digitos()
        return f'{self.cpf_tem[0:3]}.{self.cpf_tem[3:6]}.{self.cpf_tem[6:9]}-{self.cpf_tem[9:11]}'

    def valida_cpf(self):
        self.digitos()
        if self.cpf == self.cpf_tem:
            return True
        else:
            return False

    def digitos(self):
        soma1 = 0
        soma2 = 0
        for indice, valor in enumerate(range(10, 1, -1)):
            soma1 += valor * int(self.cpf_tem[indice])

        digito1 = self.conta_cpf(soma1)
        self.cpf_tem += digito1
        for indice, valor in enumerate(range(11, 1, -1)):
            soma2 += valor * int(self.cpf_tem[indice])
        digito2 = self.conta_cpf(soma2)
        self.cpf_tem += digito2
        return digito1 + digito2


if __name__ == '__main__':
    valida = ValidadorCPF()
    valida.recebe_cpf(valida.gera_cpf())
    print(valida.valida_cpf())
