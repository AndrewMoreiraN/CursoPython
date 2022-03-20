from account import Account


class ContaPoupanca(Account):

    def withdraw(self, value):
        if value > self.balance:
            print(f'{value} é maior que o permitido.')
            return
        self.balance -= value
        self.details()
