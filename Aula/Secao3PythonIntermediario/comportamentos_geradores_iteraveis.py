nome = 'Andrew'
iterador = iter(nome)
gerador = (letra for letra in nome)

try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
except:
    pass

print('cade os valores')
for valor in iterador:
    print(valor)

print('cabou iterador')

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('Dentro do for')

for letra in gerador:
    print(letra)
