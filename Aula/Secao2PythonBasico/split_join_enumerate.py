"""
Split, Join, Enumerate em Python
* Split - Dividir uma string #str
* Join - Juntar uma lista #str
* Enumerate - Enumerar elementos da lista #iteráveis
"""
string1 = 'O Brasil é o país do futebol, o Brasil é penta.'
lista_1 = string1.lower().split(' ')
lista_2 = string1.lower().split(', ')
print(lista_2)
print(lista_1)
palavra = ''
contagem = 0
for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}')
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é "{palavra}" {contagem} vezes')

string2 = ', '.join(lista_1)
print(string2)

for indice, valor in enumerate(lista_1, 0):
    print(valor, indice)

lista = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for indice1, valor in lista:
    print(indice1, valor)
