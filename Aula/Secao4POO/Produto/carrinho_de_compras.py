class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []

    def inserir_produto(self, produto):
        self.__produtos.append(produto)

    def lista_produto(self):
        for produto in self.__produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.__produtos:
            total += produto.valor
        return total
