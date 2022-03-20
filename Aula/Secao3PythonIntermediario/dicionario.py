# importa o modulo copy para copiar um dicionario para outra variavel
import copy

# dicionarios contem pares dentro do mesmo, um sendo uma chave unica que indica um valor,
# a ordenaçao do dicionario é em ordem de atribuiçao,
d1 = {'chave': 'valor'}  # define a chave ou key 'chave' e o valor ou value para esta chave 'valor'
d1 = {'chave': 'valor', 'chave': 'valor', 'chave': 'valor final da chave'}
# outro meio de criar um dicionario atraves do metodo dict
d1 = dict(chave1='valor da chave1', chave2='valor da outra chave')
# atribuiçao de uma nova chave e um valor a ela
d1['nova_chave'] = 'valor da nova chave'
# chaves sao unicas entao a chave fica com o ultimo valor atribuido a ela


d1 = {
    'chave1': 'valor',
    'chave2': 'outro valor',
    'chave3': 'tupla',
}

print(d1)
print(d1['nova_chave'], 'valor dentro da chave "nova_chave"')
print(d1['chave1'], 'valor dentro da chave "chave1"')
print(d1['chave2'], 'valor dentro da chave "chave2"')
# se a chave 'naoexiste' esta no dicionario, printe o valor que esta atribuido a ela
if 'naoexiste' in d1:
    print(d1['naoexiste'])

# outro metodo de adicionar uma nova chave e valor ao dicionario atraves do metodo update
d1.update({'nova_chave': 'novo valor'})

# deletar do dicionario d2 a chave 'str' e o valor que ela contem
del d1['str']

print(d1, 'd1 apos deleter chave "str" junto com seu valor')

# se algo esta na chave 'str' print o valor
if d1.get('str') is not None:
    print(d1.get('str'))

# len funciona para saber a quantidade de pares que o dicionario contem
print(len(d1))
# verifica se 'str' é uma chave de d1
print('str' in d1, 'se "str" é uma das chaves de d1')
# verifica se 'str' é uma chave de d1
print('str' in d1.keys(), 'se "str" é uma das chaves de d1')
# verifica se 'valor' é um dos valores que d1 contem
print('valor' in d1.values(), 'se "valor" é um dos values de d1')

# imprimi todas as chaves do dicionario
for k in d1:
    print(k, 'chaves do dicionario')

for k in d1.keys():
    print(k, 'chaves do dicionario')

for v in d1.values():
    print(v, 'valores do dicionario')

for k, v in d1.items():
    print(k, v, 'chaves e valores do dicionario')

clientes = {
    'cliente1': {
        'nome': 'Andrew',
        'sobrenome': 'Moreira',
    },
    'cliente2': {
        'nome': 'Marli',
        'sobrenome': 'Moreira',
    },
    'cliente3': {
        'nome': 'Isis',
        'sobrenome': 'Moreira',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Andrew', 'Moreira']}
# v = d1.copy() #isto faz apenas uma copia de referencia, caso modificada o original tambem é
v = copy.deepcopy(d1)  # isto faz uma nova variavel com os mesmo valores e não modifica o original
print(v == d1)
v[1] = 'Andrew'
print(d1, 'd1')
print(v, 'v')
print(v == d1)
v['d'][0] = 'Pedro'
print(v['d'][0])
print(d1, 'd1')
print(v, 'v')

lista_lista = [
    [1, 2],
    [2, 3],
    [3, 4],
]
lista_tupla = [
    (1, 2),
    (2, 3),
    (3, 4),
]

tupla_lista = (
    [1, 2],
    [2, 3],
    [3, 4],
)

tupla_tupla = (
    (1, 2),
    (2, 3),
    (3, 4),
)

# a funçao dict() pode transformar tuplas ou listas que tenham pares em dicionarios
print(dict(lista_lista))
print(dict(lista_tupla))
print(dict(tupla_lista))
print(dict(tupla_tupla))

d1 = {
    1: 2,
    3: 4,
    5: 6,
}
d2 = {
    'a': 'b',
    'b': 'c',
    'c:': 'd',
}
print(d1, 'd1')
print(d2, 'd2')
# junta um dicionario a outro com sua ordem sendo adicionada apos a do outro que esta fazendo o update
d1.update(d2)
print(d1, 'd1 update')
# remove uma chave e valor do dicionario(valor da chave é informado)
d1.pop(1)
print(d1, 'removido chave 1')
# remove o ultimo item do dicionario nao precisando indicar a chave
d1.popitem()
print(d1, 'removido ultima chave')
