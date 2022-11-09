# str = 문자열
# float = 실수
# int = 정수

#관계 연산자 
# >, < , <=, >=, ==
#참,거짓 판단
#이항 연산자

#논리 연산자
#and, or , not

#제어문
#프로그램의 흐름을 제어
#if, for, while, break, continue



print('='*20)
print('철도 지연 배상금 계산기입니다.')
ticket = int(input('승차권 구매 금액을 입력하세요. >>> '))
option = int(input('환불 수단을 선택하세요 [1. 현금환불  2. 할인증] >>> '))
late = int(input('지연 시간을 입력하세요(분단위로 입력) >>> '))
if late < 20:
    print('지원 배상금이 없습니다.')
elif option == 1:
    if late >= 60:
        money0 = int(ticket*0.5)
    elif late >= 40:
        money0 = int(ticket*0.25)
    elif late >= 20:
        money0 = int(ticket*0.125)
    print("지연배상금은 {:,}원입니다.".format(money0))
else:
    if late >= 60:
        money0 = ticket
    elif late >= 40:
        money0 = int(ticket*0.5)
    elif late >= 20:
        money0 = int(ticket*0.25)
    print("지연할인증은 {:,}원입니다.".format(money0)) 