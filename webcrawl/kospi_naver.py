import requests
from bs4 import BeautifulSoup

class Kospi_naverCrawler:
    def __init__(self, url):
        self.url = url

    def scrap(self):
        # url = 'https://finance.naver.com/sise/'
        html = requests.get(self.url).text
        soup = BeautifulSoup(html,'lxml')
        tags = soup.select("span[id=KOSPI_now]")
        print("Naver 현재 KOSPI 지수는 {0} 입니다.".format(tags[0].text))