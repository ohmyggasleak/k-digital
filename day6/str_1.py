# st = "Have a nice day"
# print(st[3:6])
# for i in st:
#     print(i,end="")
# print()

# for i in range( len(st) ):
#     print(st[i],end="")

# st = "Python test. 그리고 programming 할만하다 ^^"
# print(st)
# print(st.upper()) #대문자 변경
# print(st.lower()) #소문자 변경
# print(st.swapcase()) # 상호변경, 대/소문자
# print(st.title()) #단어의 첫번째 대문자로 변경

# st = "NevEr -eVer 110gIVe up"
# # st = st.lower()
# st = st.title() #얘만 써도 됨
# print(st)
# print(st.count('e'))
# print(st.count('ev'))
# print(st.startswith('Ne'))
# print(st.startswith('ne'))
# print(st.endswith('up'))
# print(st.endswith('Up'))
# print(st.upper().isupper())
# print(st.islower())

# st= "It is a fun Python class"
# print(len(st))
# print(st.count('a'))
# print(st.count('s'))

# st= "Have a nice day"
# print(st)
# print(st.find('day'))
# print(st.index('day'))
# print(st.find('dddd')) # 존재하지않으면 -1 
# # print(st.index('dddd')) #에러
# print(st.find('a'))   #1
# print(st.find('a',2)) #5
# print(st.find('a',6)) #13
# print(st.find('a',14))#-1

# num=st.find('a')
# print(st.find('a'))  
# print(st.find('a',num+1))

# num = st.find('a',num+1)
# print(st.find('a',num+1))

# st = "Have a nice day Have a nice day Have a nice day Have a nice day Have a nice day Have a nice day"
# print("a 개수",st.count('a'))
# #1
# cnt=0
# li=[]
# for i in st:
#     if i=='a':
#         li.append(cnt)
#     cnt+=1
# print("index:",li)
# #2
# li=[]
# i=0
# num=-1
# while i<st.count('a'):
#     num=st.find('a',num+1)
#     if num>=0:
#         li.append(num)
#     else:
#         break
#     i+=1
# print(li)
# #3
# li=[]
# num=-1
# for i in range(st.count('a')):
#     num=st.find('a',num+1)
#     li.append(num)
# print(li)

# #ab로 시작하는 문자열, test로 끝나는 문자열
# li=['AbCe test123','acd dfg', 'a123 TEST 123','123 TEst']
# for i in li:
#     if i.lower().startswith('ab'):
#         print(i)
#     if i.lower().endswith('test'):
#         print(i)

# st = '   파이썬    '
# print(f"*{st}*")
# print(f"*{st.strip()}*")

# name = input("이름 입력: ")
# print("이름: ",name)
# if name.strip() == "홍길동":
#     print("인증통과")
# else:
#     print("인증실패!!!")

# st = '+++파 이 썬 +++'
# print(st)
# print(st.strip("+"))
# print(st.rstrip("+"))
# print(st.lstrip("+"))

# st='2015/04/02'
# print(st)
# print(st.replace("/","."))
# print(st.replace(st[0:4], "2022"))

# st = '''
# 김개똥 -2017년 03월 24일
# 홍길동구리 -2015년 04월 02일
# 선우선녀 -2018년 05월 14일
# '''

# num=-1
# for i in range(st.count('년')) :
#     num=st.find("년",num+1)
#     st=st.replace("-",":")
#     st=st.replace(st[num-4:num],'1999')
# print(st)

# #1
# n=int(input("n:"))
# st=""
# for i in range(1,n+1):
#     st+=str(i)
# print(len(st))

#2

# n=int(input("n:"))
# for i in range(n):
#     li.append(input("단어입력: "))


# ls=['bc','a','dfsq','ab','asdfq']
# ls.sort()
# print(ls)
# for i in range(5):
#     for j in range(5):
#         # print(ls[i],ls[j])
#         if len(ls[i])<len(ls[j]):            
#             ls[i],ls[j] = ls[j],ls[i]
# print(ls)


# li=[4,8,2,7,6]
# for i in range(4):
#     for j in range(i+1,5):
#         if li[i]>li[j]:
#             li[i],li[j] = li[j],li[i]
# print(li)


# ls.sort()
# for i in range(len(ls)):
#     for j in range(len(ls)):
#         print(ls[i],ls[j])
        
#         if len(ls[i]) < len(ls[j]):
#             ls[i], ls[j] = ls[j], ls[i]
#         print(ls)
# print(ls)
    
# li.sort(key=len)
# print(li)

# line='Have a nice day Have a nice day Have a nice day Have a nice day Have a nice day Have a nice day'
# i=0
# while True:
#     if i!=0 and line[i].isupper():
#         print()
#     print(line[i],end='')
#     i += 1
#     if i == len(line):
#         break

