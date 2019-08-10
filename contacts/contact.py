class Contact:
    def __init__(self,n1,n2,n3,n4):
        self.n1=n1
        self.n2=n2
        self.n3=n3
        self.n4=n4

    def to_string(self):
        t = '이름: {0} \n전화번호: {1} \n이메일: {2} \n주소: {3} '.format(self.n1, self.n2, self.n3, self.n4)
        return t