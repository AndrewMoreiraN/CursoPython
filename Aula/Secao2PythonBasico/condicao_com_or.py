nome = input('Qual o seu nome? ')

# if nome:
#     print(nome)
# else:
#     print('Você não digitou nada =(')

print(nome or 'Você não digitou nada =(')

a = 0
b = None
c = False
d = []
e = {}
f = 22

variavel = a or b or c or d or e or f
print(variavel, 'Pegará o primeiro valor não vazio')
