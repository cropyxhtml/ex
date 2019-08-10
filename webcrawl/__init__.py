from webcrawl.controller import Controller

if __name__=="__main__":
    # View
    print('a, Paliament:')
    print('b, Bugs_Music:')
    print('n, Kospi_Naver:')
    print('k, Krx_Sumsung:')
    print('ns, Naver_Stock:')
    print('nm, Naver_Movie:')
    print('log, Naver Login:')
    print('0, 종료:')

    # Input
    flag = input("Select keyword :").strip()

    # Execute
    exe = Controller()
    exe.exec(flag)
