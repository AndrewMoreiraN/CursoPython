import random
import re


def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def soma_numeros_primeiro(cnpj):
    total_soma = 0
    for index, i in enumerate(range(13, 1, -1)):
        if i > 9:
            total_soma += int(cnpj[index]) * (i - 8)
        else:
            total_soma += int(cnpj[index]) * i
    return total_soma


def soma_numeros_segundo(cnpj):
    total_soma = 0
    for index, i in enumerate(range(14, 1, -1)):
        if i > 9:
            total_soma += int(cnpj[index]) * (i - 8)
        else:
            total_soma += int(cnpj[index]) * i
    return total_soma


def retorna_digito(soma_numeros):
    if 11 - (soma_numeros % 11) > 9:
        return 0
    else:
        return 11 - (soma_numeros % 11)


def sequencial(cnpj):
    return cnpj[0] * len(cnpj) == cnpj


def valida(cnpj):
    cnpj_limpo = remover_caracteres(cnpj)
    digito1 = retorna_digito(soma_numeros_primeiro(cnpj_limpo))
    digito2 = retorna_digito(soma_numeros_segundo(cnpj_limpo))
    if (cnpj_limpo[12:] == str(digito1) + str(digito2)) and not sequencial(cnpj_limpo):
        print(f'CNPJ {cnpj} é um valor válido.')
    else:
        print(f'CNPJ {cnpj} é um valor inválido.')
    return


def gera():
    primeiro_digito = random.randint(0, 9)
    segundo_digito = random.randint(0, 9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'
    inicio_cnpj = f'{primeiro_digito}{segundo_digito}.{segundo_bloco}.{terceiro_bloco}/{quarto_bloco}-'
    cnpj_limpo = remover_caracteres(inicio_cnpj)
    inicio_cnpj += str(retorna_digito(soma_numeros_primeiro(cnpj_limpo)))
    cnpj_limpo = remover_caracteres(inicio_cnpj)
    inicio_cnpj += str(retorna_digito(soma_numeros_segundo(cnpj_limpo)))
    return inicio_cnpj


valida(gera())
