from downloader import Downloader
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

class MainApplication():
    def main(self):
        link = 'https://www.web.statistik.zh.ch/ogd/data/KANTON_ZUERICH_477.csv'
        d = Downloader(link)
        d.download()
        data = StringIO(d.data)
        df = pd.read_csv(data, sep=";")
        grouped_by_year = df.groupby(['INDIKATOR_JAHR'])
        print(grouped_by_year.std()['INDIKATOR_VALUE'])
        print(grouped_by_year.skew()['INDIKATOR_VALUE'])
        print(grouped_by_year.apply(pd.DataFrame.kurt)['INDIKATOR_VALUE'])
        years = df['INDIKATOR_JAHR'].unique()
        plt.plot(years, df.groupby(['INDIKATOR_JAHR']).mean()['INDIKATOR_VALUE'])
        plt.xticks(years)
        plt.grid()
        plt.ylabel('Value')
        plt.xlabel('Jahr')
        plt.show()
        print("neine")


def main():
    main_application = MainApplication()
    main_application.main()

if __name__ == '__main__':
    main()