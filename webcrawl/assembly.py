from bs4 import BeautifulSoup
from urllib.request import urlopen

class AssemblyCrawler:
    def __init__(self, url):
        self.url=url

    def scrap(self):
        url = urlopen(self.url)
        soup = BeautifulSoup(url, 'html.parser')
        txt - soup.find(id='summaryContentDiv').text
        print(txt)