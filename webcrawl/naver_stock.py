import requests
import pandas as pd
from bs4 import BeautifulSoup

class Naver_stockCrawler:
    def __init__(self, item):
        self.item = item

    def scrap(self):
        url = 'https://finance.naver.com/item/sise_day.nhn?code=' + self.item # {item}.format(code=self.item)
        html = requests.get(url).text
        # tr > td.2th class =" tah p11"
        soup = BeautifulSoup(html,'lxml')
        # print(html)
        tag = soup.find_all(name='span',attrs=({'class':'tah p11'}))
        # tag = soup.select("span[class=tah p11]")
        for i in tag:
            print(str(i.text))
if __name__ == '__main__':
    item='005930'
    url = 'https://finance.naver.com/item/sise_day.nhn?code=' + item  # {item}.format(code=self.item)
    html = requests.get(url).text
    # tr > td.2th class =" tah p11"
    soup = BeautifulSoup(html, 'lxml')
    # print(html)
    # tag = soup.find_all(name='span', attrs=({'class': 'tah p11'}))
    tag = soup.select("td.num + .p11.tah")
    for i in tag:
        print(str(i.text))

