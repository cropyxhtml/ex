from calculator.model import CalculatorModel

class CalculatorController:
    def __init__(self,n1,n2):

        self.calc=CalculatorModel(n1, n2)

    def exec(self, op):
        if op == '+':
            result = self.calc.a1()
        elif op == '-':
            result = self.calc.a2()
        elif op == '*':
            result = self.calc.a3()
        elif op == '/':
            result = self.calc.a4()
        return result

