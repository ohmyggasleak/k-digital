# print("test python")

#총 3개의 인자를 받는 calc(num1,num2,op)
def calc(num1,num2,op):
    if op == "+":
        print(num1+num2)
    elif op == '-':
        print(num1-num2)
    elif op == '*':
        print(num1*num2)
    elif op == '/':
        print(num1/num2)

calc(5,10,'/')






#vsum 함수를 만들어 인자로 전달된 모든 값을 더하는 함수를 만드시오

#vsum(1,2) 결과값:3
#vsum(1,2,3) 결과값:6
#vsum(1,2,3,4,5) 결과값 : 15
