from bankaccount import BankAccount

class YouthAccount(BankAccount):
    def __init__(self, age: int, name='', surname='', address='', 
                currency='CHF', interest=1.001, maximum=100000):
        print(age)
        if age > 25:
            raise ValueError('The customer is too old')
        super().__init__(age=age, name=name, surname=surname, address=address, currency=currency,
            interest=interest, maximum=maximum)

    def __str__(self) -> str:
        return 'Youth Account'