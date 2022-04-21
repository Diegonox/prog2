from bomservice import BomService
from prettytable import PrettyTable

class BomMenu():
    def __init__(self):
        pass

    def main(self):
        bom_service = BomService()
        data = bom_service.get()
        t = PrettyTable(['Mat', 'Cost'])
        total_sum = 0
        for key in data:
            t.add_row([key, data[key]])
            total_sum += data[key]
        t.add_row(['Sum', total_sum])
        print(t)

if __name__ == '__main__':
    menu = BomMenu()
    menu.main()