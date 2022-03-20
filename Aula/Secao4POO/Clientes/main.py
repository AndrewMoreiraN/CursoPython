from cliente import Cliente
from cliente_vip import ClienteVip

cliente1 = Cliente('Andrew', 26)
cliente1.inserir_endereco('Palhoça', 'SC')
cliente2 = Cliente('Mãe', 26)
cliente2.inserir_endereco('Florianópolis', 'SC')
cliente3 = Cliente('Computador', 26)
cliente3.inserir_endereco('h', 'SP')

cliente1.lista_endereco()
cliente2.lista_endereco()
cliente3.lista_endereco()

cliente4 = ClienteVip('Andrew', 12, 'Moreira')
cliente4.falar()
