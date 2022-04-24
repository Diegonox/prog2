import requests
  
# download csv from link
class Downloader():
    def __init__(self, link):
        self.link = link
        self.data = None

    def download(self):
        r = requests.get(self.link)
        r.encoding = r.apparent_encoding
        self.data = r.text

def main():
    link = 'https://www.web.statistik.zh.ch/ogd/data/KANTON_ZUERICH_477.csv'
    d = Downloader(link)
    d.download()
    
if __name__ == '__main__':
    main()