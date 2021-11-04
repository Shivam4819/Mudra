import pandas as  pd
import dataframe_image as dfi
from pandas.core.reshape import tile
import seaborn as sns 
import matplotlib.pyplot as plt


class TopCompany:

    def get_top_company():
        stocklist= pd.read_csv('StockList.csv')
        data= stocklist.pivot_table(columns=['Sector'], aggfunc='size')
        top=data.nlargest(5).to_frame().reset_index()
        top=top.iloc[0]['Sector']
        companylist= stocklist[(stocklist['Sector']==top)]
        f= companylist.pivot_table(columns=['Company'],aggfunc='size')
        ds=f.nlargest(15).to_frame().reset_index()
        ds=ds.rename(columns={0:'Number of time'})
        dfi.export(ds, 'Companylist.png')
        print(ds)
        return "job done"