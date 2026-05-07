class Account:

    def __init__(self, amount):
        self.__balance = amount
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = Account(1000)

print(account.get_balance())