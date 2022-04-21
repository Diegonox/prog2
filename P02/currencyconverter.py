import requests

class CurrencyConverter():
    api = 'https://open.er-api.com/v6/latest/'
    from_currency = 'CHF'

    def get_currency_from_api(self, from_currency=from_currency):
        r = requests.get(self.api + from_currency)
        return r.json()

    def get_rate(self, to_currency, from_currency=from_currency):
        currency_dict = self.get_currency_from_api(from_currency=from_currency)
        return currency_dict['rates'][to_currency]

    def convert_currency(self, amount, to_currency, from_currency=from_currency):
        currency_dict = self.get_currency_from_api(from_currency=from_currency)
        rate = currency_dict['rates'][to_currency]
        return amount * rate, rate

def main():
    cc = CurrencyConverter()
    rate = cc.get_rate(to_currency='USD', from_currency='CHF')
    print(f'CHF/USD {rate}')
    print('CHF/USD', cc.convert_currency(100, to_currency='USD', from_currency='CHF'))

if __name__ == '__main__':
    main()