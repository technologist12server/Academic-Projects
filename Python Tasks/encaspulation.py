"""class Speed:
    def __init__(self):
        self.speed = 10
s = Speed()
s.speed = 60
print(s.speed)

class Speed:
    def __init__(self):
        self.__new__speed = 80
s = Speed()
print(s.__new__speed)"""""

initial_balance = 1000.0
account_number = "123456789"

class BankAccount:
    def __init__(self, initial_balance, account_number):
        self.__account_balance = initial_balance
        self.__account_number = account_number
    
    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__account_balance

account1 = BankAccount(1000.0, "123456789")
account1.deposit(500.0)
account1.withdraw(200.0)
print("Final account balance:", account1.get_balance())
