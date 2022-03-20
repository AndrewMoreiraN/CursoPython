"""
Combinations, Permutations e Product - Itertools
Combinação - ordem não importa
Permutação - ordem importa
ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import product, combinations, permutations

pessoas = ['Andrew', 'Mae', 'Mouse', 'Teclado', 'monitor']
print('COMBINATIONS')
for grupo in combinations(pessoas, 4):
    print(grupo)

print('\nPERMUTATIONS')
for grupo in permutations(pessoas, 3):
    print(grupo)

print('\nProduct')
for grupo in product(pessoas, repeat=1):
    print(grupo)
