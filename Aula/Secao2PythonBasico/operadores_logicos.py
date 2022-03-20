"""
Operadores lógicos
and, or, not
in e not in

and = ambos verdadeiros é verdadeiro
or = um verdadeioro é verdadeiro
not = troca de verdadeiro ou falso para o inverso
in = se contem por exemplo 'a' in 'escola'
not in = oposto do in
"""

usuario = input('Digite o usuario. ')
senha = input('Digite a senha. ')

usuario_bd = 'isiserrada'
senha_bd = '090711isis'

if usuario == usuario_bd and senha == senha_bd:
    print('Valores certos, você está logada.')
else:
    print('Valores incorretos.')
