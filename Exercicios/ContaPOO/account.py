from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency, account, balance):
        self.__agency = agency
        self.__account = account
        self.__balance = balance

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value):
        self.__account = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @property
    def agency(self):
        return self.__agency

    @agency.setter
    def agency(self, value):
        self.__agency = value

    @abstractmethod
    def withdraw(self, value): pass

    def deposit(self, value):
        self.balance += value
        self.details()

    def details(self):
        print(f'Agência: {self.agency} '
              f'Account: {self.account} '
              f'Balance: {self.balance}')
