from textmining.model import SamsungReport

if __name__ == "__main__":
    sam = SamsungReport()
    # sam.download()
    # print(sam.extract_noun()) # @staticmethod 사용시 instance 없어도 가능
    print(sam.remove_stopword())