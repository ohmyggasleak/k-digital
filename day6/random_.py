'''
범위를 지정해서 특정 범위의 무작위 수를 뽑는다
'''
# import random

# for i in range(5):
#     print(random.random(),end=" ")
# print()

# for i in range(5):
#     print(random.randrange(0,3),end=" ")
# print()

# #로또프로그램 1~45 사이의 무작위 중복되지 않는 6개의 수
# ls = []
# while len(ls)<6:
#     num=random.randrange(1,46)
#     if ls.count(num)>=1:
#         continue
#     else:
#         ls.append(num)
# print(ls)

# s = set()
# while len(s)<6:
#     s.add(random.randrange(1,46))
# s=sorted(s)
# print(s)

# #updown 게임
# from random import randrange

# rank=set([200])
# while True:
#     print("1.게임시작 2.최고기록 확인 3.종료")
#     num=input(">>>:")
#     cnt=0
#     if num == '1':
#         com=randrange(1,100)
#         print("com:",com)
#         while True:
#             cnt+=1
#             su=int(input("수 입력:"))
#             if su<com:
#                 print("up")
#             elif su>com:
#                 print("down")
#             else:
#                 if min(rank)>cnt:
#                     print("최고기록 갱신")
#                 rank.add(cnt)
#                 print("정답")
#                 break
                    
#     elif num == '2':
#         if len(rank)==0:
#             print("게임 먼저 진행하세요")
#         else:
#             print("최고기록 :",min(rank))
#     elif num =='3':
#         print("프로그램이 종료됩니다.")
#         break
#     else:
#         print("잘 못 입력하셨습니다.")

#야구게임
# from random import randrange
# rank={200}
# while True:
#     print("1.게임시작 2.최고기록 확인 3.종료")
#     choice = input(">>>")
#     com = set()
#     while len(com)<3:
#         com.add(randrange(1,10))
#     if choice == '1':
#         com=sorted(com)
#         cnt=0
#         while True:
#             s,b,o=0,0,0
#             user=[]
#             print("com:",com)
#             for i in range(3):
#                 user.append(int(input("수입력: ")))
#             print(user)
#             for i in range(3):
#                 if com[i]==user[i]:
#                     s+=1
#                 elif user[i] in com :
#                     b+=1
#                 elif user[i] not in com:
#                     o+=1    
#             print(f"{s}스트라이크, {b}볼, {o}아웃")
#             cnt+=1
#             if s==3:
#                 rank.add(cnt)
#                 if min(rank)>cnt:
#                     print("최고기록 갱신")
#                 break
                
#     elif choice == '2':
#         print(f"최고기록 {min(rank)}")
#     elif choice =='3':
#         print("프로그램이 종료됩니다")
#         break
#     else:
#         print("잘 못 입력하셨습니다.")


# #2
# import random
# best=100
# while True :
#     print("1.게임시작 2.최고기록 확인 3.종료")
#     num=input(">>> : ")
#     if num == "1" :
#         com=[]
#         while len(com)<3:
#             x=random.randrange(1,10)
#             if com.count(x)==0:
#                 com.append(x)
#         print(f"com : {com}")

#         count=0

#         while True:
#             count+=1
#             s=0
#             b=0
#             o=0
#             for i in com:
#                 su=int(input("수 입력:"))
#                 if i==su:
#                     s+=1
#                 elif com.count(su)==1:
#                     b+=1
#                 else:
#                     o+=1
#             print(f"{s}스트라이크, {b}볼, {o}아웃")
#             if s==3:
#                 if count<best:
#                     print(f"{count}회, 최고기록 갱신")
#                     best=count            
#                 else:
#                     print(f"{count}회")
#                 break
                        
#     elif num=="2":
#         print("최고기록은 {}".format(best))
#     elif num=="3":
#         print("프로그램이 종료됩니다.")
#         break
#     else :
#         print("잘못입력하셨습니다.")

