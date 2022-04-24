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
        plt.title('Baulandpreisentwicklung im Kanton Zürich')
        plt.plot(years, df.groupby(['INDIKATOR_JAHR']).mean()['INDIKATOR_VALUE'])
        plt.xticks(years)
        plt.locator_params(axis = 'x', nbins = 10)
        plt.grid()
        plt.ylabel('Preis in 1000 CHF')
        plt.xlabel('Jahr')
        plt.show()
        
        
        new_df = df.groupby('GEBIET_NAME').mean('INDIKATOR_VALUE').reset_index()
        new_df = new_df.sort_values('INDIKATOR_VALUE')
        new_df = new_df.tail(5)
        #↓print(new_df)
        
        #Bar plot expensive locations in ZH
        plt.bar(new_df['GEBIET_NAME'],new_df['INDIKATOR_VALUE'])
        plt.ylim(1100,1400)
        plt.ylabel('Preise pro m2')
        plt.title('Teuerste Gemeinden')
        plt.show()
        
        # Bar Plot cheap locations in ZH
        cheap_df = df.groupby('GEBIET_NAME').mean('INDIKATOR_VALUE').reset_index()
        cheap_df = cheap_df.sort_values('INDIKATOR_VALUE')
        cheap_df = cheap_df.head(5)
        
        plt.bar(cheap_df['GEBIET_NAME'],cheap_df['INDIKATOR_VALUE'])
        plt.title('Günstigste Gemeinden in Zürich')
        plt.ylabel("Preise pro m2")
        plt.ylim(140,250)
        plt.show()
        
        
        #filter cheapest and most expensive locations to watch the price development
        compare_df = df.loc[df['GEBIET_NAME'] == 'Fischenthal']
        plt.plot(compare_df['INDIKATOR_JAHR'],compare_df['INDIKATOR_VALUE'])
        plt.title('Fischenthal (günstigste Gemeinde')
        plt.ylabel('Preis pro m2')
        
        compare_df = df.loc[df['GEBIET_NAME'] == 'ZÃ¼rich']
        plt.plot(compare_df['INDIKATOR_JAHR'],compare_df['INDIKATOR_VALUE'])
        plt.title('Fischenthal (günstigste Gemeinde')
        
        
        
        
        
    
        




def main():
    main_application = MainApplication()
    main_application.main()

if __name__ == '__main__':
    main()