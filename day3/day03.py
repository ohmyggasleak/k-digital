# import sys, os  #경로 안내하려면 필요한 코드 
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# import day2.day02
# print("현재 페이지")



#터미널 윈도우 입력키
#cls 전체 창 지우기
#pause 계속하려면 <Enter> 키를 누르십시오.:
#calc 계산기
#exit 종료 
#mspaint 그림판
#보통 컴퓨터 내에서 0이면 성공, 1이면 실패, -1이면 악성 의미

#while 반복종료 단축키 : 터미널에서 ctrl+c

# import os

# #data = 0 #초기화
# data = None #초기화(아무것도없음)

# while True:
#     print("="*30)
#     print("1.데이터 입력")
#     print("2.데이터 출력")
#     print("3.종료")
#     print("="*30)
#     num = int(input(">>> : "))
#     if num == 1:
#         data = input("데이터 입력 =>")
#     elif num == 2 :
#         if data==None:
#             print("저장 데이터 없음")
#         else:
#             print("입력 데이터 : ",data)
#         os.system("pause")      
#     elif num ==3:
#         os._exit(1)
#     else:
#         print("잘 못 입력하셨습니다. ")
    
#     os.system("cls")

# #문제
# import os
# sum_score = None
# name = None
# while True:
#     print("="*30)
#     print("1.학생 이름 입력")
#     print("2.성적 3과목(국,영,수) 입력")
#     print("3 학생 이름 출력")
#     print("4.합계 출력")
#     print("5.평균 출력")
#     print("6.종료")
#     print("="*30)
#     data = input(">>> :")
#     if data == '1':
#         name = input("학생 이름을 입력해주세요 : ")
#     elif data == '2':
#         k_l = int(input("국어점수 : "))
#         e_l = int(input("영어점수 : "))
#         math = int(input("수학점수 : "))
#         sum_score = k_l + e_l + math
#     elif data == '3':
#         if name == None :
#             print("초기화면 1번 학생이름 입력부터 해 주십시오.")
#         else:
#             print("학생의 이름은",name,"입니다.")

#         os.system('pause')
#     elif data == '4':
#         if sum_score ==None:
#             print("2.성적부터 입력해주세요.")
#         else:
#             print("성적의 합은",sum_score,"입니다.")
#         os.system('pause')
#     elif data == '5':
#         if sum_score ==None:
#             print("2.성적부터 입력해주세요.")
#         else:
#             print("성적의 평균은",round(sum_score/3,2),"입니다.")
#         os.system('pause')
#     elif data == '6':
#         print("프로그램이 종료됩니다.")
#         os._exit(1) 
#     else:
#         print("다시 확인하고 입력해주세요.")

#     os.system('cls')


# 반복문
# - 어떤 내용을 반복하고자 하는 경우
# - 규칙적으로 값이 변경 된다면
# for 변수 in range(초기값, 비교값, 증감값)

# #1~10까지의 합을 구하시오
# result =0
# for i in range(1,11):
#     result+=i
# print("합:",result)
# #1~30 5의 배수 때 띄어쓰기
# for i in range(1,31):
#     print(i,end="\t")
#     if i%5==0:
#         print()

# #수를 입력 받아 1~입력 받은 수 까지 짝수의 합과 홀수의 합을 구하시오.
# num = int(input("수를 입력하시오: "))
# a=0 #짝수
# b=0 #홀수
# for i in range(1,num+1):
#     if i%2==0:
#         a+=i
#     else: 
#         b+=i
# print("짝수의합:",a,"홀수의합",b)


# 두 수를 입력 받아 입력 받은 두 수의 범위 안의 합을 구하시오:
# 1입력,10입력 =>55
# 10입력,1입력 =>55
# #1
# num1=int(input("수입력: "))
# num2=int(input("수입력: "))
# sum_n = 0
# if num1>=num2:  
#     num1, num2= num2, num1
# for i in range(num1,num2+1):
#         sum_n+=i
# print("{}~{}의 합{}".format(num1,num2,sum_n))

# #2    
# li = list(map(int,input("두수입력: ").split()))
# li=sorted(li)
# sum_n =0
# for i in range(li[0],li[1]+1):
#     sum_n+=i
# print(sum_n)

# st = "It is a fun Python class"
# a_c=0
# s_c=0
# cnt=0
# for i in st:
#     cnt+=1
#     if i=='a':
#         a_c+=1
#     elif i == 's':
#         s_c+=1
# print("총 개수:{}\na 개수:{}\ns 개수:{}".format(cnt,a_c,s_c))
# print("총 개수:{}\na 개수:{}\ns 개수:{}".format(len(st),st.count('a'),st.count('s')))        

#나이트문제
# n ='c2'
# y_ = ['a','b','c','d','e','f','g','h']
# for i in range(8):
#     if n[0] == y_[i]:
#         y=i+1
# x=int(n[1])

# dx = [1,-1,1,-1,2,2,-2,-2]
# dy = [2,2,-2,-2,1,-1,1,-1]

# cnt=0

# for i in range(8):
#     nx = x+dx[i]
#     ny = y+dy[i]
#     if nx>=1 and ny>=1 and nx<=8 and ny<=8:
#         cnt+=1

# print(cnt)

# total_seat = 30
# count=0
# while True:
#     print("="*10,"좌석 예약 프로그램","="*10)
#     people = int(input("일행 수"))
#     print("+","-"*20,"+")
#     if total_seat<0:
#         print("좌석이 부족합니다.")
#         print("예약 가능 {}자리 남았습니다.".format(total_seat))
#     else:
#         print("|{}부터 {}번 좌석입니다.|".format(count+1,count+people))
#         print("+","-"*20,"+")
#         total_seat -= people
#         count+=people
#         print("예약 가능 {}자리 남았습니다.".format(total_seat))
#         if total_seat ==0:
#             print("모든 좌석이 예약되었습니다. 예약을 종료합니다.")  
#             break


