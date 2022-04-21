from bankaccount import BankAccount
from savingaccount import SavingAccount
from youthaccount import YouthAccount
from typing import List
from taxreport import TaxReport

class AccountInformation():
    """
    Should be implemented in Bankaccount
    """
    def __init__(self, name, surname, age, address, currency):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.currency = currency

class BankApplication():
    def __init__(self):
        self.accounts = []
        self.menu()
        pass

    def account_menu(self, accounts: List[BankAccount]):
        i = 1
        selection = 0
        for account in accounts:
            print(f'{i}: {account}, iban: {account.iban}, name: {account.name}, surname: {account.surname}, balance: {account.balance}')
            i += 1
        while True:
            try:
                selection = int(input('To select an account press the corresponding number: '))
                selection -= 1
                if selection in range(0, len(accounts)):
                    break
                else:
                    print('Number is out of range!')
            except:
                print('That\'s not a valid option!')
        return selection

    def create_youth_account(self):
        print('Creating youth account but first we need some of your information')
        account_information = self.account_information_menu()
        try:
            print(account_information.age)
            youth_account = YouthAccount(name=account_information.name, surname=account_information.surname,
                                        age=account_information.age, address=account_information.address, currency=account_information.currency)
            return youth_account
        except ValueError:
            print('You are too old for this account type. Maybe try with a savings account')
            return

    def create_saving_account(self):
        print('Creating savings account but first we need some of your information')
        account_information = self.account_information_menu()
        savings_account = SavingAccount(name=account_information.name, surname=account_information.surname,
                                        age=account_information.age, address=account_information.address, currency=account_information.currency)
        return savings_account

    def account_information_menu(self):
        name = str(input('Name: '))
        surname = str(input('Surname: '))
        age = 0
        while True:
            try:
                age = int(input('Age: '))
                break
            except:
                print('That\'s not a valid option!')
        address = str(input('address: '))
        # Should show the available currencies to the user
        currency = str(input('Currency: '))
        return AccountInformation(name, surname, age, address, currency)

    def deposit_on_account(self, account: BankAccount):
        while True:
            try:
                amount = float(input('Amount to deposit: '))
                account.deposit(amount)
                break
            except:
                print('That\'s not a valid option!')

    def withdraw_on_account(self, account: BankAccount):
        while True:
            try:
                amount = float(input('Amount to withdraw: '))
                account.withdraw(amount)
                break
            except:
                print('That\'s not a valid option!')

    def menu(self):
        current_account = 0
        while True:
            user_choice = ''
            print('Welcome to this small bank application')
            if 0 != len(self.accounts):
                print(f'Current selected account: {self.accounts[current_account]}, iban: {self.accounts[current_account].iban},'
                    + f' name: {self.accounts[current_account].name}, surname: {self.accounts[current_account].surname}, balance: {self.accounts[current_account].balance}'
                    + f' {self.accounts[current_account].currency}')
                print('To select an account press "s"')
                print('To deposit to the current account press "d"')
                print('To withdraw to the current account press "w"')
                print('To close the current selected account press "c"')
            print('To create an youth account press "y"')
            print('To create a savings account press "a"')
            print('To generate a tax report press "t"')
            print('To exit the application press "x"')
            while True:
                try:
                    user_choice = str(input('Your choice: ')).lower()
                    break
                except:
                    print('That\'s not a valid option!')
            print('-------------------------------------------')
            if user_choice == 's':
                current_account = self.account_menu(self.accounts)
            elif user_choice == 'y':
                youth_account = self.create_youth_account()
                if youth_account:
                    self.accounts.append(youth_account)
            elif user_choice == 'd':
                self.deposit_on_account(self.accounts[current_account])
            elif user_choice == 'w':
                self.withdraw_on_account(self.accounts[current_account])
            elif user_choice == 'a':
                self.accounts.append(self.create_saving_account())
            elif user_choice == 'c':
                self.accounts[current_account].close_account()
            elif user_choice == 't':
                TaxReport.generate_converted(bankapplication=self, year=2022, to_currency='CHF')
            elif user_choice == 'x':
                break
            print('-------------------------------------------')
            print()

def main():
    bankapplication = BankApplication()
    bankapplication.menu()
    
if __name__ == '__main__':
    main()