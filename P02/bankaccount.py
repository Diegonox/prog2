import random

class BankAccount():
    def __init__(self, age, name='', surname='', address='', currency='CHF', interest=0,
                maximum=100000):
        self.age = age
        self.generate_iban()
        self.balance = 0
        self.currency = currency
        self.name = name
        self.surname = surname
        self.address = address
        self.interest = interest
        self.maximum = maximum
        self.is_active = True
    
    def generate_iban(self):
        self.iban = 'CH'
        for i in range(0, 12):
            self.iban += str(random.randint(0, 9))

    def pay_interest(self):
        self.balance = self.balance * self.interest

    def print_balance(self):
        print(f'Current balance: {self.currency} {self.balance}')

    def deposit(self, amount):
        if not self.is_active:
            print('Can\'t deposit as the account is not active')
            return
        if self.balance + amount <= self.maximum:
            self.balance += amount
            return self.balance
        else:
            print('Could not deposit the money as it exceeds the max limit')
            return self.balance

    def withdraw(self, amount):
        if not self.is_active:
            print('Can\'t withdraw as the account is not active')
            return
        if self.balance - amount >= 0:
            self.balance -= amount
            return self.balance
        else:
            print('Could not make the payment as the account doesn\'t have enough money!')
            return self.balance
        
    def close_account(self):
        self.withdraw(self.balance)
        self.is_active = False


def main():
    account1 = BankAccount('CH1234', 'Diego', 'Fontana', 'test address')
    account1.deposit(10000)
    account1.print_balance()
    account1.withdraw(5000)
    account1.print_balance()
    account1.close_account()
    account1.withdraw(5000)
    account1.deposit(5000)
    account1.print_balance()
    
    
if __name__ == "__main__":
    main()