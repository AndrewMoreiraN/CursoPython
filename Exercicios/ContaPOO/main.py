from bank import Bank
from client import Client
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

banco = Bank()

cliente1 = Client('Luiz', 30)
cliente2 = Client('Maria', 18)
cliente3 = Client('João', 50)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 254137, 0)
conta3 = ContaPoupanca(1212, 254138, 0)

cliente1.add_account(conta1)
cliente2.add_account(conta2)
cliente3.add_account(conta3)

banco.add_client(cliente1)
banco.add_account(conta1)

banco.add_client(cliente2)
banco.add_account(conta2)

if banco.authenticator(cliente1):
    cliente1.account.deposit(0)
    cliente1.account.withdraw(20)
else:
    print('Cliente não autenticado.')

print('####################')

if banco.authenticator(cliente2):
    cliente2.account.deposit(0)
    cliente2.account.withdraw(20)
else:
    print('Cliente não autenticado.')
