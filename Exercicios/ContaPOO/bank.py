class Bank:
    def __init__(self):
        self.__account = []
        self.__agency = [1111, 2222, 3333]
        self.__client = []

    @property
    def agency(self):
        return self.__agency

    @property
    def client(self):
        return self.__client

    def add_client(self, value):
        self.__client.append(value)

    @property
    def account(self):
        return self.__account

    def add_account(self, value):
        self.__account.append(value)

    def authenticator(self, cliente):
        if cliente not in self.client:
            return False
        if cliente.account not in self.account:
            return False
        if cliente.account.agency not in self.agency:
            return False

        return True
