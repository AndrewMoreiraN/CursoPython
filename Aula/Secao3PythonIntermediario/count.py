"""
count - Itertools
"""
from itertools import count

contador = count(start=5, step=-2)

nome = 'andrew'

for valor in contador:
    print(round(valor, 2))

    if valor >= 20 or valor <= -20:
        break

contador2 = count()

lista = ['a', 'b', 'c', 'd']
lista = zip(contador2, lista)
print(list(lista))
