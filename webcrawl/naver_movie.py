from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

class Naver_movieCrawler:
    def __init__(self, url):
        self.driver = webdriver.Chrome(executable_path='C:/Users/ezen/PycharmProjects/tensorflow190803/webcrawl/data/chromedriver')
        self.driver.get(url)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

    def scrap(self):
        html = self.soup.prettify()
        print(html)
        all_divs=self.soup.find_all('div',attrs={'class':'tit3'})
        print(all_divs)
        arr = [div.a.span.string for div in all_divs]
        for i in arr:
            print(i)
        self.driver.close()
