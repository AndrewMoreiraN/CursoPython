from Aula.Secao3PythonIntermediario.dados import lista, pessoas, produtos


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


nova_lista = list(map(lambda x: x * 2, lista))
nova_lista2 = [x * 2 for x in lista]
print(lista)
print(nova_lista)
print(nova_lista2)

novos_produtos = map(aumenta_preco, produtos)
for produto in novos_produtos:
    print(produto)

precos = map(lambda p: p['preco'], novos_produtos)
for preco in precos:
    print(preco)

nomes = map(lambda p: p['idade'] * 1.2, pessoas)
for pessoa in nomes:
    print(pessoa)
