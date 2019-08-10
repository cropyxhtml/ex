from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugsCrawler:
    def __init__(self, url):
        self.url=url

    def scrap(self):
        url = urlopen(self.url)
        soup = BeautifulSoup(url, 'html.parser')
        n_artist = 0
        n_title = 0
        for i in soup.find_all(name='p',attrs=({'class':'artist'})):
            n_artist +=1
            print(str(n_artist)+ '위')
            print('아티스트 :'+i.find('a').text)
        print('-'*20)
        for i in soup.find_all(name='p', attrs=({'class': 'title'})):
            n_title += 1
            print(str(n_title) + '위')
            print('제목:' + i.find('a').text)

