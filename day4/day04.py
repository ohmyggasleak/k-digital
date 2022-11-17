# #구구단 만드세요
# for i in range(2,10):
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j),end="\t")
#     print()

# #상위문 하위 포문
# for i in range(5):
#     print("상위포문 {}일때 하위 포문:",end="")
#     for j in range(5):
#         print("{}".format(i*j),end = " ")
#     print()

# # 2중 for문 5배수 점프 숫자나열
# k=1
# for i in range(1,6):
    
#     for j in range(5):
#         print(j+k,end="\t")
#     print()
#     k+=5

# for i in range(0,5):
#     for j in range(1,6):
#         print(j+5*i,end="\t")
#     print()

# i=0
# while i<5:
#     print(i,"종속문장")
#     i += 1
# print("다음 문장")

# for i in range(5):
#     print(i,"종속문장")
# print("다음 문장")

# i=1
# odd, even =0 , 0
# while i <= 10:
#     if i%2 ==0:
#         even += i
#     else:
#         odd += i
#     i+=1
# print(f"1~10까지의 짝 합: {even}")
# print(f"1~10까지의 짝 합: {odd}")


# odd, even =0 , 0
# for i in range(1,11):
#     if i%2 ==0:
#         even += i
#     else:
#         odd += i
#     i+=1
# print(f"1~10까지의 짝 합: {even}")
# print(f"1~10까지의 짝 합: {odd}")


#DEBUGING
'''
f5 : 디버깅 실행 모드
f9 : 브레이크 포인트
f11 : 한줄씩 실행
f10 : 한줄씩 실행
shift + f5 : 디버깅 종료
# '''
# sum_=0
# for i in range(100000):
#     sum_ += i 
# print(sum_)
# print(sum_)
# print(sum_)
# print(sum_)

# for i in range(5):
#     print("실행")
#     for k in range(3):
#         print("종속")
#     print("끝")


# #while 
# i=1
# flag =True
# while flag:
#     print(i,"종속문장",end =" ")
#     if i ==5:
#         flag = False
#     i+=1
'''
break : 반복문을 빠져나올 경우 사용
continue : 반복문 위로 올려보낸다
'''
# print("===break===")
# i=0
# while i<=5:
#     i+=1
#     if i==3:
#         # break
#         print("3333")
#     print(i,".출력")
# print("다음 문장")


# print("===continue===")
# i=0
# while i<=5:
#     i+=1
#     if i==3:
#         continue
#         print("3333")
#     print(i,".출력")
# print("다음 문장")

# print("===while else===")
# i=0
# while i<5:
#     i+=1
#     print(i,"종속문장")
#     if i==2:
#         break
# else:
#     print("else실행")
# print("다음 문장")

#while과 while else 이용, break, continue 사용
#10~20 사이의 숫자만 입력 받아 1부터 입력받은 수의 합
# i=0
# sum_=0
# x=0
# while x<30:
#     n=int(input("10~20 사이의 숫자 입력:"))    
#     if n<10 or n>20:
#         print("잘 못 입력 다시")
#         continue
#     else:
#         for i in range(1,n+1):
#             sum_ += i
#             x=35
        
# else:
#     print(f"1~{n}까지의 합: {sum_}")

# for i in range(0,3,1):
#     for k in range(0,5,1):
#         if k==3:
#             break
#         print(f"i:{i},k:{k}")

# i=0
# while True:
#     k=0
#     while True:
#         print(f"i:{i},k:{k}")
#         k+=1
#         if k==3:
#             break
#     i+=1
#     if i==3:
#         break

# #자판기
# import os
# coffe = 200
# cocoa = 250
# change = None
# price = int(input("요금을 투입하세요: "))
# while True:
#     print("{:=^30}".format("커피 자판기"))
#     print("1. 커피(200)   2.코코아(250)  3. 반환 4.종료")
#     menu = input("메뉴를 선택하세요>>> ")
#     if menu == '1':
        
#         change=price-coffe
#         if change >=0:
#             print("맛있게 드세요")
#             price=change
#         else:
#             print("잔액 부족")
#         os.system('pause')
#     elif menu == '2':
#         change = price-cocoa
#         if change>=0:
#             print("맛있게 드세요")
#             price=change
#         else:
#             print("잔액 부족")
#         os.system('pause')
#     elif menu == '3':
#         if change<=0:
#             print("반환될 금액이 없습니다.")
#         else:
#             print(f"반환 금액 : {change}")
#             change = 0
#             price = 0
#         os.system('pause')
#     elif menu == '4':
#         print("프로그램이 종료됩니다.")
#         break
#     else:
#         print("잘 못 입력하셨습니다.")
#         os.system('pause')
#     os.system('cls')

# #1에서부터 입력된 어떤 수까지 내에 있는 소수를 찾는 프로그램
# n=int(input("수입력: "))
# print("소수:",end=" ")
# for i in range(2,n+1):
#     cnt=0
#     for j in range(1,i+1):
#         if i%j==0:
#             cnt+=1
#     if cnt==2:
        # print("{}".format(i),end = " ")



# #피라미드 만들기

# num = int(input('피라미드의 높이'))

# for i in range(1):
#     for j in range(1,num+1):
#         print(" "*(num-j)+"□"*(j*2-1))

# #중국집 메뉴판 만들기
# money=0
# z,zz,b,t =0,0,0,0
# while True:
#     print("{:=^30}".format("중국식 메뉴판"))
#     print("1.자장면:6000원\n2.짬뽕:7000원\n3.볶음밥:8000원\n4.탕수육:20000원\n5.실행 종료")
#     num = input("무엇을 주문하시겠습니까?")
#     if num=='1':
#         print("자장면 1개 추가.")
#         money += 6000
#         z+=1
#     elif num == '2':
#         print("짬뽕 1개 추가.")
#         money += 7000
#         zz+=1
#     elif num == '3':
#         print("볶음밥 1개 추가")
#         money += 8000
#         b+=1
#     elif num == '4':
#         print("탕수육 1개 추가")
#         money += 20000
#         t+=1
#     elif num == '5':
#         print("총 주문내역은 자장면{}개,짬뽕{}개,볶음밥{}개,탕수육{}개로 총 가격{:,}입니다.".format(z,zz,b,t,money))
#         break
#     else:
#         print("다시 입력해주세요") 

# #1분 미만 스탑워치 만들기
# import os
# from time import sleep
# print('{:=^}'.format('1분미만 제한 스탑워치'))
# second = int(input('스탑워치 시간 입력(초) >>> '))

# if second >=60:
#     print("제한 시간 초과")
# else:    
#     for i in range(0,60):
#         for j in range(60):
#             print(i,':',j)
#             os.system('cls')
#             sleep(1/60)
#         if i==(second-1):
#             print(i+1,': 00')
#             os.system('pause')
#             break



