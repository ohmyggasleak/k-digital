'''
turtle 모듈 이용해서 도형 그리기
정수 입력 받아서 3을 입력하면 정삼각형, 4를 입력하면 정사각형을 만드는 함수만들기

hint)
정삼각형 그리는 방법
import turtle as t 
t.left(120) #(왼쪽으로 120도 꺾는다.)
t.forward(100) #(앞으로 100만큼 간다.)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.mainloop() #그린 모양유지
'''

# import turtle as t
# n=int(input("몇 각형으로 그려드릴까요? (정수로 입력)"))
# def shape():
#     for i in range(n):
#         t.left(360/n)
#         t.forward(100)
#     t.mainloop()

# shape()





# num = int(input("첫번째 수 입력: "))
# f_num=num
# repeatNum = int(input("반복할 수 입력: "))
# cnt = int(input("반복할 횟수 입력: "))
# oper = input("연산자(+,-,*,/)")

# def calc():
#     global num, repeatNum
#     for i in range(cnt):
#         if oper == '+':
#             num+=repeatNum    
#         elif oper == '-':
#             num-=repeatNum
#         elif oper == '/':
#             num/=reapeatNum
#         elif oper == '*':
#             num*=repeatNum
#     return num
# num_=calc()
# print("{}에서 {}을 {}번 {}한 값은 {}입니다.".format(f_num,repeatNum,cnt,oper,num_))






# #입력, 연산, 출력 함수를 만들고 수(num)를 입력했을 때, 짝수만 리스트에 넣어서 결과 값을 내는 함수를 만드시오.
# #함수 예) input_, even_list, print_list
# #힌트 for문, append

li=[]
def input_():
    return int(input("수 입력: "))

def print_list():
    print(li)

num=input()