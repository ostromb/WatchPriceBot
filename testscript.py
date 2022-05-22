from bs4 import BeautifulSoup
import requests


def main():
    file = open('dataBuk','w')
    link = 'https://www.bukowskis.com/sv/auctions/638/'
    pages = 1
    url = '%s%s'% (link,pages)
    data = requests.get(url)
    html = BeautifulSoup(data.text, 'html.parser')
    articles = html.select("div.c-live-lot-show-lot")
    print(articles)
    #file.write()
main()