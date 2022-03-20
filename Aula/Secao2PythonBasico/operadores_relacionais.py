"""
Operadores Relacionais
== igualdade
!= diferente
> maior que
< menor que
>= maior ou igual a
<= menor ou igual a
"""

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

idade = int(idade)

idade_menor = 20
idade_maior = 30

if idade_menor <= idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')
