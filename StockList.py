import pandas as pd
import requests, sys
from bs4 import BeautifulSoup

class StockList:

    def get_stock_from_csv():
        stock= pd.read_csv("FundNameList.csv")
        top_data=stock
        s= StockList()
        return s.whole_stock_list(top_data)

    def whole_stock_list(self,final):
        data = final
        final_df_list=pd.DataFrame()
        s = StockList()
        for i in range(len(data)):
            urls = data['search_id'][i]
            fund = data['fund_name'][i]
            extract = s.extract_stock(urls,fund)
            final_df_list = final_df_list.append(extract)
            print('----',i,'----')
         
        final_df_list.to_csv('StockList.csv',index=False)

        if len(final_df_list)>0:
         return {"message-":"Data stored to csv successfully","length of data":str(len(final_df_list))}
        else:
         return {"message-":"Data not stored ","length of data":str(len(final_df_list))}



    def extract_stock(self,lastpart,fund):
        try:
            url = 'https://groww.in/mutual-funds/' + lastpart
            page = requests.get(url)
        except Exception as e:
            error_type, error_obj, error_info = sys.exc_info()
            print('Error-', url)
            print(error_type, 'line:', error_info.tb_lineno)

        soup = BeautifulSoup(page.text, 'html.parser')
        lists = soup.find_all('td', attrs={'class': 'fs14'})

        CompanyName = lists[::4]
        Sector = lists[1::4]
        Instrument = lists[2::4]
        Assets = lists[3::4]

        FinalDic = {}
        output = pd.DataFrame()
        for i in range(len(CompanyName)):
            FinalDic = {
                'FundName': fund,
                'Company': CompanyName[i].text,
                'Sector': Sector[i].text,
                'Instrument': Instrument[i].text,
                'Assets': Assets[i].text

            }

            output=output.append(FinalDic,ignore_index=True)

        return output


    
