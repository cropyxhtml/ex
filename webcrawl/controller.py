from webcrawl.assembly import AssemblyCrawler
from webcrawl.bugsmusic import BugsCrawler
from webcrawl.kospi_naver import Kospi_naverCrawler
from webcrawl.krx import KrxCrawler
from webcrawl.naver_stock import Naver_stockCrawler
from webcrawl.naver_movie import Naver_movieCrawler
from webcrawl.naver_login import NaverLogin

class Controller:
    def __init__(self):
        pass

    def exec(self, flag):
        if flag == 'a':
            url = 'http://likms.assembly.go.kr/bill/billDetail.do?billId=PRC_R1N9J0N1X0Y9A1O8S3R5Z3J3K9O8N7'
            a = AssemblyCrawler(url)
            a.scrap()
        elif flag == 'b':
            url = 'https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20190810&charthour=11'
            b = BugsCrawler(url)
            b.scrap()
        elif flag == 'n':
            url = 'https://finance.naver.com/sise/'
            n = Kospi_naverCrawler(url)
            n.scrap()
        elif flag == 'k':
            url = 'https://kind.krx.co.kr/disclosureSimpleSearch.do?method=disclosureSimpleSearchMain'
            k = KrxCrawler(url)
            k.scrap()
        elif flag == 'ns':
            ns = Naver_stockCrawler('005930')
            ns.scrap()
        elif flag == 'nm':
            url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
            nm = Naver_movieCrawler(url)
            nm.scrap()
        elif flag == 'log':
            url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
            login = NaverLogin(url)
            login.auto_login()

        elif flag == '0':
            print("Exit")

        # return result