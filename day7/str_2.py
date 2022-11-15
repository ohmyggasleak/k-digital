# st = 'Never ever give up'
# print(st)
# print(st.split())
# print(st.split("e"))

# st = "안녕하세요 오늘 2300/5/14 날씨는 error 춥다"
# sp_li = st.split()
# year = sp_li[2].split('/')
# del(sp_li[4])
# del(sp_li[2])
# sp_li.insert(2,year[0]+"년"+year[1]+"월"+year[2]+"일")
# st=""
# for i in sp_li:
#     st += i + " "
# print(st)
# print(" ".join(sp_li))

# st='''
# 안녕하세요
# 안녕하세요
# 안녕하세요
# 안녕하세요
# '''
# print(st)
# print( st.splitlines() )
# print(st.split('\n'))

# st='123'
# test = '%'
# print(test.join(st))
# print("$".join(st))
# print(st.join("안녕하세요"))

# li = ["","123","456"]
# print("그래".join(li))

# st = 'python'
# print(st)
# print(st.center(10)) #가운데 정렬
# print(st.center(10,"-")) 

# print(st.ljust(10)) #왼쪽 정렬
# print(st.ljust(10,'a'))

# print(st.rjust(10)) #오른쪽 정렬
# print(st.rjust(10,'a'))

# print(st.zfill(10))


# accountBook = "shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000"
# a_b = accountBook.split(', ')

# print('item'.ljust(10),end="")
# print('date'.ljust(10),end="")
# print('$(price)'.ljust(10))
       
# for i in range(len(a_b)):
#     z=a_b[i].split()
#     for j in range(len(z)):
#         if j==0:
#             print(z[j].ljust(10),end="")
#         elif j==1:
#             print(z[j].ljust(10),end="")
#         else:
#             print("{:,}".format(int(z[j])).join(kk).ljust(10)) 


# st = 'python te12st 1234'
# print(st.isdigit()) #숫자로만 구성
# print(st[9:11].isdigit())

# print(st.isalpha()) #영어로 구성
# print(st[:6].isalpha())

# print(st.isalnum()) #알파벳 + 숫자로만 구성
# print(st[7:13].isalnum())

# print(st.islower()) #소문자
# print(st.isupper()) #대문자
# print(st.isspace()) #공백


#문제1
info = """
jo 9abc08-3022023
cho 900402-1011232
test 1234567-1234567 
lee 980908-3a2b0c3
kim 900514-2022023
"""
# li=info.splitlines()
# del[li[0]]
# k=0
# for i in li:
#     k=info.find('-',k+1)
#     x=i.split('-')
#     if x[0][-6:].isdigit() and x[1].isdigit():
#         info = info.replace(info[k+1:k+8],"*******")    
# print(info)

# # T
# info = """
# jo 9abc08-3022023
# cho 900402-1011232
# test 1234567-1234567 
# lee 980908-3a2b0c3
# kim 900514-2022023
# """
# # print( info )
# k=0
# for i in range( info.count('-') ):
#     k=info.find('-' , k+1)
#     if info[k+1:k+8].isdigit() and \
#                 not info[k-7:k].isdigit() and \
#                             info[k-6:k].isdigit():
#         info = info.replace(info[k+1:k+8] , '*******' )
# print( info )
