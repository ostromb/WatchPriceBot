import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
def main():
    #link = input('Enter HTML: ')
    link = 'https://www.kaplans.se/sv/auktioner/4035'
    pages = 6
    my_data = []
    for i in range (1,pages+1):
        try:
            print('%s?p=%s'% (link,i))
            url = '%s?p=%s'% (link,i)
            data = requests.get(url)
            html = BeautifulSoup(data.text, 'html.parser')
            articles = html.select('div.list-item')
            for article in articles:
                try:
                    try:
                        watchcontent = article.select('p')[0].get_text()
                        article.select('h3')[0].get_text()
                        watchmodel = re.findall('PIC nr\. ([^,]+)',watchcontent)[0]
                        watchbrand = article.select('h3')[0].get_text().split('\n')[2]
                        watchmodel = watchbrand + " " + watchmodel
                    except:
                        watchcontent = article.select('p')[0].get_text()
                        article.select('h3')[0].get_text()
                        watchmodel = re.findall('Ref nr\. ([^,]+)',watchcontent)[0]
                        watchbrand = article.select('h3')[0].get_text().split('\n')[2]
                        watchmodel = watchbrand + " " + watchmodel
                    try:
                        watchcontent = article.select('p')[0].get_text()
                        article.select('h3')[0].get_text()
                        cert = re.findall('(cert)',watchcontent)[0]
                    except:
                        cert = 'n/a'
                    try:
                        priceRE = article.select('.currency-newline')[0].get_text()
                        price = re.findall('(\d+\s*\d+)',priceRE)[0]
                        price = float(''.join(price.split()))*1.2
                        my_data.append({"Watchmodel":watchmodel,"Price":price,"Certified":cert})
                    except Exception as e: 
                        priceRE = article.select('.info-short')[0].get_text()
                        price = re.findall('(\d+\s*\d+)',priceRE)[0]
                        price = float(''.join(price.split()))*1.2
                        my_data.append({"Watchmodel":watchmodel,"Price":price,"Certified":cert})
                    
                except:
                    pass
                    
                
        except Exception as e:
            break
  
    df = pd.DataFrame(my_data)
    print(df)
    df.to_csv("infosheet.csv")
    
main()