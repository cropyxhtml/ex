import requests
import pandas as pd
from bs4 import BeautifulSoup

class KrxCrawler:
    def __init__(self, url):
        self.url = url

    def scrap(self):
        html = requests.get(self.url).text
        soup = BeautifulSoup(html,'lxml')
