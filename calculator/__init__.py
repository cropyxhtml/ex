from calculator.controller import CalculatorController
if __name__=='__main__':
    n1 = int(input('첫번째 수'))
    n2 = int(input('두번째 수'))
    a=CalculatorController(n1,n2)
    op = input('operator')
    result = a.exec(op)
    print('계산결과는 %d'%result)
