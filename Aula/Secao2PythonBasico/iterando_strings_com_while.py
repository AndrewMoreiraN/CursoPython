frase = 'o rato roeu a roupa do rei de roma'
tamanho_da_frase = len(frase)  # 34 indices 0-33
contador = 0
nova_string = ''

while contador < tamanho_da_frase:
    # print(frase[contador], contador)
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += frase[contador]
    print(nova_string)
    contador += 1

print(nova_string)
