from carrinho_de_compras import CarrinhoDeCompras
from produto import Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('camiseta', 50)
p2 = Produto('caneca', 'R$15')
p3 = Produto('Carro', '12000')

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)

carrinho.lista_produto()
print(carrinho.soma_total())
