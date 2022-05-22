import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def searcher():
    
    df = pd.read_csv('infosheet.csv')
    lowestList = []
    offerList = []
    
    for model in df['Watchmodel']:
        try:
            print(model)
            url = 'https://www.chrono24.com/search/index.htm?query=%s&dosearch=true&searchexplain=1&watchTypes=&accessoryTypes='%model
            data = requests.get(url)
            html = BeautifulSoup(data.text, 'html.parser')
            article = html.select('script')[19]
            
        
            try:
                webjson = json.loads(article.get_text())
                for d in webjson['@graph']:
                    if d.get('lowPrice'):
                        lowPriceRE = d.get('lowPrice')
                        lowPrice = re.findall('(\d+)',lowPriceRE)[0]
                        lowPrice = float(''.join(lowPrice.split()))*9.7
                    if d.get('offerCount'):
                        offerRE = d.get('offerCount')
                        offer = re.findall('(\d+)',offerRE)[0]
                        offer = int(''.join(offer.split()))
                    
                    
                    
                lowPriceRE = [d.get('lowPrice') for d in webjson['@graph'] if d.get('lowPrice')][0]
                
                lowPriceRE = [d.get('lowPrice') for d in webjson['@graph'] if d.get('lowPrice')][0]
            except:
                offer = 0
                lowPrice = 0.0
            offerList.append(offer)
            lowestList.append(lowPrice)
            
        except:
            pass
        #file2.write(html.text)

    df['Lowest Price'] = lowestList

    df['Price Difference'] = df['Lowest Price'] - df['Price']
    df['Discount'] = df['Lowest Price']/df['Price']
    df['Volume'] = offerList
    print(df)
    df.to_csv("PriceOverviewK4092.csv")
searcher()