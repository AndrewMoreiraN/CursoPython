from person import Person


class Client(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__account = None

    @property
    def account(self):
        return self.__account

    def add_account(self, value):
        self.__account = value
