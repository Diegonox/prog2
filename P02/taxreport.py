from typing import List
from bankaccount import BankAccount
from currencyconverter import CurrencyConverter


class TaxReport():
    def __init__(self):
        pass

    def generate(bankaccounts: List[BankAccount], year):
        print(f'Tax report {year} for fiscal year {year-1}')
        for bankaccount in bankaccounts:
            print(f'** {bankaccount} ** {bankaccount.balance} {bankaccount.currency}')

    # generate tax report for all accounts in the list and convert them to the given currency
    # use the given currency converter to convert the balance to the given currency
    # print the tax report
    def generate_converted(bankapplication, year, to_currency):
        print(f'Tax report {year} for fiscal year {year-1}')
        currency_converter = CurrencyConverter()
        for bankaccount in bankapplication.accounts:
            converted_amount, rate = currency_converter.convert_currency(amount=bankaccount.balance, to_currency=to_currency, from_currency=bankaccount.currency)
            print(f'** Conversion rate {bankaccount.currency}/{to_currency}: {rate} **')
            print(f'** {bankaccount} ** {converted_amount} {to_currency}')