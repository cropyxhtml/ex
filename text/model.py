from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import re
class SamsungReport:
    def __init__(self):
        pass

    @staticmethod
    def read_file():
        okt = Okt()
        okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        filename = 'C:/Users/ezen/PycharmProjects/tensorflow190803/text/data/kr-Report_2018.txt'
        with open(filename, 'r', encoding='utf-8') as f:
            texts = f.read()
        return texts

    @staticmethod
    def extract_hangeul(texts):
        temp = texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ ㄱ-힣]+')
        temp = tokenizer.sub('', temp)
        return temp

    @staticmethod
    def change_token(texts):
        tokens = word_tokenize()
        print(tokens[:7])