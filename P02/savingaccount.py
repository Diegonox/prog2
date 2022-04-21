from bankaccount import BankAccount

class SavingAccount(BankAccount):
    def __init__(self, age: int, name='', surname='', address='', 
                currency='CHF', interest=1.02, maximum=100000, fees=1.02, withdraw_limit=2000):
        super().__init__(age=age, name=name, surname=surname, address=address, currency=currency, interest=interest,
                maximum=maximum)
        self.fees = fees
        self.withdraw_limit = withdraw_limit
        self.current_withdraw_per_month = 0
    
    def __str__(self) -> str:
        return 'Savings Account'

    def withdraw(self, amount):
        if not self.is_active:
            print('Can\'t withdraw as the account is not active')
            return
        self.current_withdraw_per_month += amount
        if self.current_withdraw_per_month >= self.withdraw_limit:
            print('Can\'t withdraw as the account exceeded its withdraw limit')
            return
        if self.balance - amount >= 0:
            self.balance -= amount
            return self.balance
        else:
            self.balance -= amount * self.fees
            return self.balance

    def reset_withdraw_limit(self):
        self.current_withdraw_per_month = 0