from Aula.Secao3PythonIntermediario.dados import pessoas, produtos, lista


def fiiltra(produto):
    if produto['preco'] >= 554:
        produto['e_caro'] = True
        return True


pe = pessoas
pr = produtos
lis = lista

nova_lista = filter(lambda x: x > 5, lista)
nova_lista2 = filter(fiiltra, produtos)
for x in nova_lista2:
    print(x)
