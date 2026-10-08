#1. Define Bank Account
class BankAccount:
    def __init__(self):
        self.balance = 0 
    def  deposit (self, amount):
        self.balance += amount
    def withdraw (self, amount):
        if amount > self.balance:
            print("Error : Insufficient funds!")
        else:
            self.balance -= amount
    def check_balance(self):
        return self.balance
acc = BankAccount()
acc.deposit()
acc.check_balance()
acc.withdraw(100)
