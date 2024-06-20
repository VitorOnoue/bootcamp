class Account:
    def __init__(self, balance):
        self._balance = balance # _balance is private
    
    def deposit(self, value):
        self._balance += value

    def withdraw(self, value):
        self._balance -= value

    def get_balance(self):
        return self._balance

account = Account(100)
# wrong thing to do:
account._balance += 100
print(account._balance)

# correct thing to do
account.deposit(100)
print(account.get_balance())