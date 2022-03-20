"""
Desempacotamento de listas em Python
"""
lista = ['Andrew', 'João', 'Japa', 1, 2, 3, 4, 5, 6, 7, 8]
n1, n2, n3, *outra_lista, ultimo_da_lista = lista

print(n1, n2, n3, outra_lista, ultimo_da_lista)
