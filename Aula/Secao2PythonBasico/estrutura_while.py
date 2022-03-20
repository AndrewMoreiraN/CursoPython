"""
while em python
utilizado para realizar ações enquanto
uma condição for verdadeira.

"""
while True:
    nome = input('Qual o seu nome? ')
    if nome[:5] == 'marli' or nome[:5] == 'Marli':
        continue
    if nome == '':
        break
    print(f'Olá {nome}!')
print('Acabou.')

x = 0
while x < 100:
    print(x)
    x += 5
