class CalculatorModel:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def a1(self):
        result=self.n1+self.n2
        return result

    def a2(self):
        result=self.n1-self.n2
        return result

    def a3(self):
        result=self.n1*self.n2
        return result

    def a4(self):
        result=self.n1/self.n2
        return result