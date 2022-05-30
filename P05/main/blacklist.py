

import csv
from genericpath import exists
# to do/think about:
# the language of the blacklist should be defined or saved in different languages? 
# the csv file should be saved in folder 'data'

class BlackList:

    def __init__(self):
        pass

    def create_blacklist(self): #this function can also be used to reset de blacklist

        with open ('blacklist.csv', 'w') as blacklist:
            fieldnames = ['city', 'country'] 
            writer = csv.DictWriter(blacklist, fieldnames=fieldnames)
            writer.writeheader()
        

    def insert_city(self, city, country):

        with open('blacklist.csv', "a", newline="") as blacklist:
            writer = csv.writer(blacklist)
            writer.writerow([city, country])

    def check_city(self, city): 
        # checks if the city exists in the blacklist and returns True or False. 
        
        is_in_list = False
        cities = []
        with open('blacklist.csv', 'r') as blacklist:
            rows = csv.reader(blacklist)
            for row in rows:
                if city in str(row):
                    is_in_list = True
        return is_in_list


if __name__ == '__main__':
    f = BlackList()
    f.create_blacklist()
    f.insert_city('Berlin', 'Deutschland')
    print(f.check_city('Berlin'))



        

