contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break
    acumulador += contador
    contador += 1
else:
    print('Cheguei no else')
print('Passei do while')

contador = 1
acumulador = 1
while contador <= 10:
    print(contador, acumulador)
    acumulador += contador
    contador += 1
else:
    """só é executado qunado a expressao do while for falsa
            caso ele seja pulado com o break nao sera executado"""
print('Cheguei no else')
print('Passei do while')
