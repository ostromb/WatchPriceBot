import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
def main():
    #link = input('Enter HTML: ')
    link = 'https://www.bukowskis.com/sv/auctions/638/'
    pages = 129
    my_data = []
    for i in range (1,pages+1):
        try:
            print('%s%s'% (link,i))
            url = '%s%s'% (link,i)
            data = requests.get(url)
            html = BeautifulSoup(data.text, 'html.parser')
            #print(data.text)
            articles = html.select("div.c-live-lot-show-lot")
            for article in articles:
                try:
                    try:
                        watchbrand = article.select('h1')[0].get_text().split(",")[0]
                        watchmodel = article.select('p')[0].get_text().split("\n")[6]
                        watchmodel = re.findall(('(\d+)'),watchmodel)[0]
                        watchmodel = watchbrand + " " + watchmodel
                        print(watchmodel)
                        price = article.select('div.c-live-lot-show-info__final-price-amount')[0].get_text()
                        price = re.findall(('(\d+\s*\d*)'),price)[0]
                        price = float(''.join(price.split()))*1.225
                        print(price)
                        cert = "n/a"
                        my_data.append({"Watchmodel":watchmodel,"Price":price,"Cert":cert})
                    except:
                        pass
                        
                    
                except:
                    pass
                    
                
        except Exception as e:
            break
  
    df = pd.DataFrame(my_data)
    print(df)
    df.to_csv("infosheet2.csv")
    
main()