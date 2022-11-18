#list
# -index는 0부터 시작
# -[](대괄호)으로 표현

# ls =[500,200,300,400]
# print(ls)
# print(ls[0], ls[3])
# ls = [0, 0, 0, 0]
# for i in range(4):
#     ls[i] = int(input(f"{i}.수 입력 :"))
#     # s=f"안녕하세요{ls}입니다"
#     # s="안{}녕{}하세요.".format(100,200)
#     # print(str(i)+".수 입력 : ")
#     # print(f"{i}.수 입력")
# print("합: ",sum(ls))

# s='abcd'
# for i in s:
#     print(i)
# for i in ls:
#     print(i)

# #같은공간 사용 (얕은복사 예)
# ls = [10,20,30,40]
# arr = ls # 얕은복사
# arr[0] = '안녕'
# print(ls," : ",id(ls))
# print(arr," : ",id(arr))
#출력결과  ['안녕', 20, 30, 40]  :  2399077480448
#         ['안녕', 20, 30, 40]  :  2399077480448


#깊은복사 예
# ls = [10,20,30,40]]
# arr = ls[:] # 깊은복사 (주의 : list안에 list는 얕은복사가 됨. deepcopy를 써야함)
# arr = ls.copy() #깊은복사(주의 : list안에 list는 얕은복사가 됨. deepcopy를 써야함)
# import copy
# arr = copy.deepcopy(ls)
# arr[0] = '안녕'
# print(ls," : ",id(ls))
# print(arr," : ",id(arr))
#출력결과  [10, 20, 30, 40]  :  1791290324992
# #         ['안녕', 20, 30, 40]  :  1791291350208

# ls = [10,20,30]
# arr= [40,50,60]
# # print(ls)
# # print(arr)
# # arr02 = ls +arr
# # print(arr02)

# # arr03 = ls*3
# # print(arr03)
# Str = [0,0,0]
# string = [0,0,0]
# i=0
# while i<3:
#     Str[i]=ls[i]+arr[i]
#     string[i]=ls[i]*3
#     i+=1
# print("str:",Str,"\nstring:",string)

# #문제
# ls = [10,5,20,7,9,31,12,11,19,32]
# evensum=[0,0,0,0,0]
# oddsum=[0,0,0,0,0]
# result=[0,0,0,0,0]
# i=0
# while i<10:
#     if i%2==0:
#         evensum[i//2]=ls[i]
#     else:
#         oddsum[i//2]=ls[i]
#     i+=1

# i=0
# while i<5:
#     result[i]=evensum[i]-oddsum[i]
#     i+=1

# #1
# print('1번:',result)
# #2
# print('2번:',sum(evensum)-sum(oddsum))
# #3
# x=0
# invertLs=[0,0,0,0,0,0,0,0,0,0]
# for i in ls:
#     x-=1
#     invertLs[x]=i
# print('3번:',invertLs)

# #순위구하기
# score = [82,85,76,79,96]
# rank = [1,1,1,1,1]
# index=0
# for i in score:
#     for j in score:
#         if i<j:
#             rank[index]+=1
#     index+=1
# print("점수:", score)
# print("등수", rank)

# #list초기화
# ls=[]
# ls = list()

# for i in range(3):
#     value = input(f"{i}.번째 입력 : ")
#     ls.append(value)
# print("총 개수 :",len(ls))
# print("type: ",type(ls))
# print("ls: ",ls)

# ls = [30,10,20,40]
# print("ls : ",ls)
# ls.pop()
# print("pop: ",ls)
# ls.reverse()
# print("reverse:",ls)
# ls.sort()
# print("sort:",ls)

# #문제( 밑에 내용 )
# ls = [10,50,70,30,20]
# # arr : ls가 가지고 있는 값을 역으로 저장
# # sort_arr: 오른차순으로 저장(10,20,30..)
# # reverse_arr :내림차순으로 저장(70,50,30,..)

# #깊은복사 사용
# arr=ls.copy() 
# print(ls)

# arr.reverse()
# print(arr)

# sort_arr = ls.copy()
# sort_arr.sort()
# print(sort_arr)

# reverse_arr =ls.copy()
# reverse_arr.sort()
# reverse_arr.reverse()
# print(reverse_arr)

# ls=[10,20,30]
# print("ls:",ls)
# del(ls[1])
# print("del(ls.1): ", ls )

# ls.remove(30)
# print("remove(30) :", ls )

# ls=[10,20,30]
# print("ls:",ls)
# i= ls.index(20)
# print("index(20):",i)

# ls.append(100)
# print("append(100):",ls)

# ls.insert(2,500)
# print(ls)

# arr=[1,2,3,1]
# # ls = ls + arr
# ls.extend(arr)
# print(ls)

# cnt = ls.count(1)
# print(cnt)





