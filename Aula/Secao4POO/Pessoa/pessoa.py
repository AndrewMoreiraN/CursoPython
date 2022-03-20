class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.__nome = nome
        self.__idade = idade
        self.__comendo = comendo
        self.__falando = falando

    # GETTERS
    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def comendo(self):
        return self.__comendo

    @property
    def falando(self):
        return self.__falando

    # SETTERS
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @idade.setter
    def idade(self, idade):
        self.___idade = idade

    @comendo.setter
    def comendo(self, comendo):
        self.__comendo = comendo

    @falando.setter
    def falando(self, falando):
        self.__falando = falando

    def parar_falar(self):
        if self.falando:
            self.falando = False
            print('Parou de falar')
        else:
            print('Não está falando')

    def parar_comer(self):
        if self.comendo:
            self.comendo = False
            print('Parou de comer')
        else:
            print('Não está comendo')

    def comer(self, comida):
        if self.comendo:
            print(f'{self.nome} ja está comendo.')
        elif self.falando:
            print(f'{self.nome} está falando e não pode comer')
        else:
            print(f'{self.nome} começou a comer {comida}')
            self.comendo = True
            return

    def falar(self, assunto):
        if self.falando:
            print(f'{self.nome} ja está falando.')
        elif self.comendo:
            print(f'{self.nome} está comendo e não pode falar')
        else:
            print(f'{self.nome} começou a falar sobre {assunto}')
            self.falando = True
            return
