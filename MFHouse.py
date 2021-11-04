import pandas as pd
import json,http.client,uuid

class MF:

    def fund_house_data_set():
        
        maindf = []
        m=MF
        for i in range(0, 1000):
            data = m.create_data_set(i)
            df = pd.json_normalize(data['content'])
            maindf.append(df)
            print('---',i,'----')
        maindf = pd.concat(maindf)
        maindf.to_csv('FundNameList.csv', index=False)
        if len(maindf)>0:
         return {"message-":"Data stored to csv successfully","length of data":str(len(maindf))}
        else:
         return {"message-":"Data not stored ","length of data":str(len(maindf))}



    def create_data_set(pageno):
        try:
            conn = http.client.HTTPSConnection("groww.in")
            payload = ''
            headers = {
                'RemoteAddress': '[2606:4700::6812:10c4]:443',
                'ReferrerPolicy': 'strict-origin-when-cross-origin',
                'Referer': 'https://groww.in/mutual-funds/filter',
                'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
                'X-APP-ID': 'growwWeb',
                'x-platform': 'web',
                'X-REQUEST-ID': str(uuid.uuid4()),
            }
            url="/slr/v1/search/derived/scheme?available_for_investment=true&doc_type=scheme&page="+str(pageno)+"&plan_type=Direct&q=&size=16&sort_by=3"
            conn.request("GET", url, payload, headers)
            res = conn.getresponse()
            data = res.read()
            print("pageno- ",pageno)
            datas=data.decode("utf-8")
            json_data=json.loads(datas)
            return json_data
        except Exception as e:
            print("Exception-"+e)