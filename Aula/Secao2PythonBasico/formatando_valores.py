"""
Formatando valroes com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. (NÚMERO)f - Quantidade de casas decimais (float) :.1f
: (CARACTERE) (> ou < ou ^) (QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3

divisao = num_1 / num_2

print(divisao)
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = 'Andrew Moreira'

print(nome.upper(), 'upper')  # Tudo maiusculo
print(nome.lower(), 'lower')  # Tudo minusculo
print(nome.title(), 'title')  # Primeiras letras maiusculas

nome_formatado = '{n:@^20}{n:#<20}{n:%>20}'.format(n=nome)
print(f'{nome:s}')

num_3 = 1
print(f'{num_3:0>10}')  # Imprimi 0000000001

num_4 = 645
print(f'{num_4:0<10}')  # Imprimi 6450000000

num_5 = 6455
print(f'{num_5:0^10}')  # Imprimi 0006455000

num_6 = 234
print(f'{num_6:0>10.2f}')  # Imprimi 0000234.00

print(len(nome), f'{nome:#^20}', len(f'{nome:#^20}'))

print(nome_formatado, len(nome_formatado))
