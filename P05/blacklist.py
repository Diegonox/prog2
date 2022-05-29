import csv

class BlackList:

    def __init__(self):
        pass

    def create_blacklist(self):
        '''this function can also be used to erease/reset de blacklist. 
        '''

        with open ('blacklist.csv', 'w') as blacklist:
            fieldnames = ['city', 'x', 'y'] # the coordinates should help if repeated names for different cities
            writer = csv.DictWriter(blacklist, fieldnames=fieldnames)
            writer.writeheader()
        


    def insert_city(self, city, x, y): # x and y could be also arguments, if they will be used for other purposes

        with open('blacklist.csv', "a", newline="") as blacklist:
            writer = csv.writer(blacklist)
            writer.writerow([city, x, y])

if __name__ == '__main__':
    f = BlackList()
    f.create_blacklist()
    f.insert_city('Berlin', '9.99', '10.5')



        

