from time import time


def master(funcao):
    def slave(*args, **kwargs):
        print('Agora estou decorada.')
        funcao(*args, **kwargs)

    return slave


@master
def fala_oi():
    print('Oi')


@master
def outra_funcao(msg):
    print(msg)


def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'\nA função {funcao.__name__} levou {tempo:.2f}ms para executar.')
        return resultado

    return interna


@velocidade
def demora():
    for i in range(10000):
        print(i, end='')


demora()
