class Account:
    def __init__(self, balance):
        self._balance = balance # _balance is private
    
    def deposit(self, value):
        self._balance += value

    def withdraw(self, value):
        self._balance -= value

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        self._balance = value


account = Account(100)
# wrong thing to do (if no properties):
account._balance += 100
print(account._balance)
account.balance = 20
print(account._balance)