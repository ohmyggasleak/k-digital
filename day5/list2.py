# ls = [[1,2,[100,200,300],3,4],[5,6,7,8],[9,10,11,12]]

# #100출력
# print(ls[0][2][0])

# li=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# for i in li:
#     for j in i:
#         print(j,end="\t")
#     print()

# ls = [[1,2,3,4],[5,6,7,8]]
# # arr = ls[0] #얕은복사
# # arr = ls[0][:] #깊은복사
# arr = ls[0].copy() #깊은복사
# arr[1] = 1000

# print(ls)
# print(arr)

# #문제
#1
# ls_1 = [] ; ls_2 = [] ; value =1
# for j in range(3):    
#     ls_1 = []
#     for i in range(4):
#         ls_1.append(value)
#         value +=1
#     ls_2.append(ls_1)

# print(ls_2)

# for i in range(len(ls_2)):
#     for j in range(len(ls_2[i])):
#         print(ls_2[i][j],end="\t")
#     print()

# #2
# ls_1 = [] ; ls_2 = [] ; value =1
# while value<13:
#     ls_1.append(value)
#     if value%4==0:
#         ls_2.append(ls_1)
#         ls_1=[]
#     value+=1
# print(ls_2)

# #map 함수
# ls = ['10','20','30']
# s = list(map(int,ls)) #list에 넣지 않으면 class 'map'으로 저장됨.
# print(s[0]*100)
