# def sum_func(x1, x2, x3=100):
#     re = x1 + x2 + x3
#     return re
# re = sum_func(10,20)
# print("합: ",re)
# re = sum_func(10,20,30)
# print("합: ",re)

# def transfer(su=1,won=500):
#    for i in range( 1 , su ):
#        won *= 2
#    return "요금 :{}입니다".format( won )

# def disply():
#     destination = ''; su = 0
#     num = int( input('1.환승 안함\n2.환승 함\n3.장거리\n') )
#     if num == 1:
#         result = transfer()
#     elif num == 2:
#         su = int(input('환승 수 입력 : ') )
#         result = transfer( su )
#     else:
#         result = transfer( won = 10000 )
#     print( result )

# disply()


# def work_calc(work_time=240,basic_price=12000):
#     salary = work_time * basic_price
#     return salary

# def display():
#     n=input("1.기본급 2.일한 시간설정 3.시급 설정 4.시간 & 시급설정\n>>>")
#     if n == '1':
#         salary = work_calc()
#     elif n =='2' :
#         salary = work_calc(int(input("일한 시간 입력")))
#     elif n=='3':
#         salary = work_calc(basic_price=int(input("시급 입력:")))
#     else :
#         salary = work_calc(int(input("일한 시간:")),int(input("시급: ")))        
    
#     print(f"월급 : {salary:,}")

# display()










