from functools import reduce

from dados import produtos, pessoas, lista

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
soma_pessoas = reduce(lambda ac, p: p['idade'] + ac, pessoas, 0)

print(soma_lista)
print(soma_precos)
print(soma_pessoas / len(pessoas))
