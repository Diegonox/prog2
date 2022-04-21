class BankAccount():
    def __init__(self, iban: str, name='', surname='', address='', currency='CHF'):
        self.iban = iban
        self.balance = 0
        self.currency = currency
        self.name = name
        self.surname = surname
        self.address = address
        self.is_active = True

    def print_balance(self):
        print(f'Current balance: {self.currency} {self.balance}')

    def deposit(self, amount):
        if not self.is_active:
            print('Can\'t deposit as the account is not active')
            return
        if self.balance + amount <= 100000:
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