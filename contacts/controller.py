from contacts.model import ContactsModel
class ContactsController:
    def __init__(self):
        self.model=ContactsModel()
    @staticmethod
    def print_menu():
        print('1, 연락처 입력:')
        print('2, 연락처 출력:')
        print('3, 연락처 삭제:')
        print('0, 종료:')
        menu = int(input('메뉴 선택'))
        return menu

    def run(self):
        params = []
        while 1:
            menu = self.print_menu()
            if menu ==1:
                n1=input("이름\n")
                n2=input("전화번호\n")
                n3=input("이메일\n")
                n4=input("주소\n")
                t = self.model.set_contact(n1,n2,n3,n4)
                params.append(t)
            elif menu ==2:
                print(self.model.get_contacts(params))
            elif menu ==3:
                n1 = input('삭제할 이름')
                self.model.del_contact(params, n1)
            elif menu ==0:
                print('시스템 종료')
                break