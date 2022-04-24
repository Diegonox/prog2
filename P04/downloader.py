'''
Downloader for P04, downloads the data for the given link.
Diego did the Downloader class and MainApplication class
with one graph. Victor did the rest of the graphs.
''' 
__author__ = 'Diego Fontana, Velloso Etter Victor Dominik' 
__email__ = 'fontadie@students.zhaw.ch, vellovic@students.zhaw.ch'

import requests
import time, os, stat
  
class Downloader():
    '''
    Downloader class
    '''
    file_path = 'data.txt'
    def __init__(self, link):
        self.link = link
        self.data = None

    def download(self):
        '''
        Only downloads the file if the current one is older than 10 minutes
        '''
        if os.path.exists(self.file_path) and self.file_age_in_seconds() > 600:
            r = requests.get(self.link)
            r.encoding = r.apparent_encoding
            self.data = r.text
            with open(self.file_path, 'w') as text_file:
                text_file.write(self.data)
        else:
            with open(self.file_path, 'r') as text_file:
                self.data = text_file.read()

    def file_age_in_seconds(self):
        return time.time() - os.stat(self.file_path)[stat.ST_MTIME]

def main():
    link = 'https://www.web.statistik.zh.ch/ogd/data/KANTON_ZUERICH_477.csv'
    d = Downloader(link)
    d.download()
    
if __name__ == '__main__':
    main()