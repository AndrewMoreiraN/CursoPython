"""
Listas em Python
fatiamento
append = inseri um novo valor no final da lista, lista1.append('b) = lista1 + 'b'
insert = inserir algo em uma posição da lista lista1.insert(index, 'oq inserir')
pop =
del = deleta elementos de uma lista informando um índice ou fatiamento del(lista1[3:5])
clear = limpa a lista, lista1.clear()
extend = função de uma lista para colocar outra iterável no final da mesma lista1.extend(lista2) = Lista1Lista2
+ = Concatenação de listas na ordem lista1 + lista2 = lista1lista2
min = retorna o numero mínimo de uma lista
max = retorna o numero maximo de uma lista
range = retorna um objeto range, range (0 'sera inserido', 10 'terminara em 9 pois o 10 nao é incluido', 2 'step pulara de 2 em 2)
"""

# #         0    1    2    3    4
# lista = ['a', 'bacana', 'c', 'd', 'e']
# #      -  5    4    3    2    1
#
# string = 'abacanacde'
#
# print(lista)
# print(lista[1], 1)
#
# print(string)
# print(string[1], 1)
#
# lista[1] = 'babaca'
# print(lista)
# print(lista[1], 1)
#
# print(lista[::-1])


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
l1.extend(l2)
l1.append('b')
l1.insert(1, 'banana')

print(l1, 'sem del')
print(l1, 'apos del [3:6]')
print(l2)
print(l3)
del (l1[1])
del (l1[len(l1) - 1])

print(max(l1), 'max')
print(min(l1), 'min')
