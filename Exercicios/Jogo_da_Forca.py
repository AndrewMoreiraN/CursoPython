import os

secreto = input('Digite a frase ou palavra secreta: ')
erros = int(input('Número de erros: '))
os.system('cls')
digitou = []
menu = True
while menu:
    while True:
        letra = input('Digite uma letra: ')

        if len(letra) > 1:
            print('Digite apenas uma letra')
            continue

        digitou.append(letra)

        if letra in secreto:
            print(f'Contém a letra "{letra}".')
        else:
            print(f'Não contém a letra "{letra}"')
            erros += 1
            print(f'Número de erros é {erros}')
            if erros == 8:
                print('Perdeu!!!')
                break

        secreto_temp = ''
        for letra_secreta in secreto:
            if letra_secreta in digitou:
                secreto_temp += letra_secreta
            else:
                secreto_temp += '*'

        if secreto_temp == secreto and secreto == 'mae que amo tanto':
            print(f'Acerto era "{secreto}", me empresta 50R$ que preciso para ter e não gastar, Valeu S2')
            break
        elif secreto_temp == secreto:
            print(f'Completou o teste a frase era "{secreto}".')
            break
        else:
            print(secreto_temp)
        print()
    temp = input('Sair: ')
    if temp == 's':
        menu = False
