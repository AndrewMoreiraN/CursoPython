"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o
valor da função2 executada.
"""


def funcao1(funcao):
    return funcao()


def funcao2():
    return 'num1 + num2'


print(funcao1(funcao2))

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o 
valor da função2 executada. Faça a função1 executar duas funções que 
recebam um número diferente de argumentos.
"""


def funcao3(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def funcao4(num1):
    return f'Numero {num1}'


def funcao5(num1, num2):
    return f'Numeros {num1} e {num2}'


print(funcao3(funcao4, 1))
print(funcao3(funcao5, 7, 8))
