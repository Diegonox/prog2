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
        df = pd.read_csv(data, sep=";" )
        self.statistical_moments(df)
        self.price_development(df)
        self.expensive(df)
        self.cheap(df)
        self.comparison(df)
        
    
    def statistical_moments(self,df):
        grouped_by_year = df.groupby(['INDIKATOR_JAHR'])
        print(grouped_by_year.std()['INDIKATOR_VALUE'])
        print(grouped_by_year.skew()['INDIKATOR_VALUE'])
        print(grouped_by_year.apply(pd.DataFrame.kurt)['INDIKATOR_VALUE'])
        
        
    def price_development(self,df):    
        years = df['INDIKATOR_JAHR'].unique()
        plt.title('Baulandpreisentwicklung im Kanton Zürich')
        plt.plot(years, df.groupby(['INDIKATOR_JAHR']).mean()['INDIKATOR_VALUE'])
        plt.xticks(years)
        plt.locator_params(axis = 'x', nbins = 10)
        plt.grid()
        plt.ylabel('Preise pro m2')
        plt.xlabel('Jahr')
        plt.show()
        
    def expensive(self,df): 
        #Bar plot expensive locations in ZH
        new_df = df.groupby('GEBIET_NAME').mean('INDIKATOR_VALUE').reset_index()
        new_df = new_df.sort_values('INDIKATOR_VALUE')
        new_df = new_df.tail(5)
        print(new_df)
        
        
        plt.bar(new_df['GEBIET_NAME'],new_df['INDIKATOR_VALUE'])
        plt.ylim(1100,1400)
        plt.ylabel('Preise pro m2')
        plt.title('Teuerste Gemeinden')
        plt.show()
        
    def cheap(self,df):
        # Bar Plot cheap locations in ZH
        cheap_df = df.groupby('GEBIET_NAME').mean('INDIKATOR_VALUE').reset_index()
        cheap_df = cheap_df.sort_values('INDIKATOR_VALUE')
        cheap_df = cheap_df.head(5)
        
        
        plt.bar(cheap_df['GEBIET_NAME'],cheap_df['INDIKATOR_VALUE'])
        plt.title('Günstigste Ortschaften im Kanton Zürich')
        plt.ylabel("Preise pro m2")
        plt.ylim(140,250)
        plt.show()
        
        
    def comparison(self,df):
        #filter cheapest and most expensive locations to watch the price development
        compare_df = df.loc[df['GEBIET_NAME'] == 'Fischenthal']
        plt.plot(compare_df['INDIKATOR_JAHR'],compare_df['INDIKATOR_VALUE'], label = 'Fischenthal')
        plt.title('Vergleich teuerste vs günstigste Ortschaft')
        plt.ylabel('Preis pro m2')
        
        compare_df = df.loc[df['GEBIET_NAME'] == 'ZÃ¼rich']
        plt.plot(compare_df['INDIKATOR_JAHR'],compare_df['INDIKATOR_VALUE'], label = 'Zürich')
        plt.legend()
        plt.show()
        
    
def main():
    main_application = MainApplication()
    main_application.main()
    

if __name__ == '__main__':
    main()