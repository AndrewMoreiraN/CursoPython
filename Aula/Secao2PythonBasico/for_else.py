"""
For / Else em python
se nao tiver break executará o else
"""
variavel = ['Andrew', 'João', 'Japa']

for valor in variavel:
    if valor.lower().startswith('j'):
        print('Começa com "J"')
        break
else:
    print('Não existe palavras que começam com j')
