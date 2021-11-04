import pandas as  pd
from pandas.core.reshape import tile
import seaborn as sns 
import matplotlib.pyplot as plt


class Sector:

    def top_sector():
        stocklist= pd.read_csv('StockList.csv')
        data= stocklist.pivot_table(columns=['Sector'],aggfunc='size')
        data.nlargest(5).to_csv('sector.csv',header=['Count'])
        d= pd.read_csv('sector.csv')
        print(d)
        sns.barplot(x='Sector',y='Count',data=d).set_title('Top 5 Sectors')
        plt.savefig('sectors.jpg')
        plt.show()
        
        return "job done"