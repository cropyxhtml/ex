from text.model import SamsungReport

if __name__ == '__main__':
    f = SamsungReport.read_file()
    print(SamsungReport.extract_hangeul(f))