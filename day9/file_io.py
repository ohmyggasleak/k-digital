'''
사용모드
- w : 파일에 내용 출력 (write)
- r : 파일에 내용 가져오기 (read)
- wb : 텍스트가 아닌 이미지, 동영상 등, 바이너리로 처리되는 값 출력
- rb : 읽어오기
- a : 이어쓰기 (append)
'''

# #file = open("위치","모드")
# file = open("E:/김진성.k-디지털/test1.txt","w")
# st = input("출력할 내용 입력: ")
# file.write(st)
# file.close()


# file = open("E:/김진성.k-디지털/test1.txt","r")
# st = file.read()
# file.close()
# print("파일에서 얻어온 값:", st)

#스트림 : 파일을 주고받고 하는 공간 ?
#close는 스트림 구간을 끊어 자원 낭비를 막기위해사용, 보조스트림에서 close시키고 내용을 보냄 

# #
# file = open("E:/김진성.k-디지털/test.txt","w")
# name = input("이름 입력 : ")
# age = input("나이 입력 : ")
# addr = input("주소 입력 : ")

# file.write(name+'\n')
# file.write(age+'\n')
# file.write(addr+'\n')
# file.close()

# #
# write_file = open("E:/김진성.k-디지털/test1.txt","w")
# read_file = open("E:/김진성.k-디지털/test.txt","r")
# # print(read_file.read())
# write_file.write( read_file.read())
# write_file.flush() # 해당(파이썬) 저장내용을 비우고 해당파일로 내용을 보냄(스트림이 열려있는상태)

# write_file.write("반가워~~~~")
# write_file.close() 
# read_file.close()

# #메모장과 파이썬에서 한글 처리하는 방법이 다를때 encoding="utf-8" 인코딩해줘야함 아니면 오류가뜸
# #인코딩 방식중에 utf-8이 한글처리하기 제일 효율적임
# read_file = open("E:/김진성.k-디지털/abcd.txt","r",encoding="utf-8")

# print( read_file.read())
# read_file.close()


###
# read_file = open("E:/김진성.k-디지털/test.txt","r")

# st = read_file.read()
# print(st)
# print(type(st))


# s1 = read_file.readline()
# s2 = read_file.readline()
# s3 = read_file.readline()
# s4 = read_file.readline()
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# if s4 == "":
#     print("더이상 데이터 없음")

# while True:
#     s = read_file.readline()
#     if s == "":
#         print("데이터없음!!")
#         read_file.close()
#         break
#     print(s,type(s))

# read_file = open("E:/김진성.k-디지털/test.txt","r")
# s=read_file.readlines()
# print(" --- lines ---")
# print(s,type(s))
# read_file.close()

# print("-----------")
# for i in range(len(s)):
#     print(f"{i}.{s[i]}")
# print("-----------")
# for i,v in enumerate(s):  # i : 넘버링(순서번호), v : 줄마다 데이터
#     print(i,v)

# #문제
# read_file = open("E:/김진성.k-디지털/test.txt","r")
# s=read_file.readlines()
# for i,v in enumerate(s):
#     print(i,':',v.strip('\n'))
# num = int(input("수정할 번호 입력: "))
# value = input("수정할 값 입력:")

# if len(s)-1==num:
#     s[num] = value
# else:
#     s[num] = value + '\n'
# read_file.close()

# write_file = open("E:/김진성.k-디지털/test.txt","w")
# for i in s:
#     write_file.write(i)
#     print(i.strip('\n'))
# write_file.close()

# path = "E:/김진성.k-디지털/"
# import os
# fileName = input("파일명 입력 : ")
# path += fileName + ".txt"
# print("path:",path)
# print(os.path.exists(path))
# if os.path.exists(path):
#     file = open(path, "r")
#     print("----파일 읽기---")
#     print(file.read())
#     file.close()

# #회원가입 프로그램 만들기
# import os

# while True:
#     os.system('cls')
#     print("1.회원가입\n2.회원보기\n3.회원수정\n4.종료")
#     n = input(">>>")    
#     path="E:/김진성.k-디지털/회원폴더/"
#     profile_ = input("회원정보: ")
#     path += profile_+".txt"
#     TF = os.path.exists(path) 
#     if n=='1':                
#         if TF:
#             print("이미 회원정보가 있습니다.")
#         else:
            
#             profile = open(path,"w")
#             profile.write(input("아이디 입력:")+'\n')
#             profile.write(profile_+'\n')
#             profile.write(input("나이 입력: ")+'\n')
#             profile.write(input("주소 입력: "))
#             profile.close()
#         os.system('pause')
#     elif n== '2':
#         if TF :
#             profile_read = open(path,'r')
#             li=profile_read.readlines()
#             for i in li:
#                 print(i.strip("\n"))
#             profile_read.close()
#         else:
#             print("회원가입부터 진행해주세요.")
        
#         os.system('pause')
#     elif n== '3':
#         if TF :
#             profile_read = open(path,'r')
#             s=profile_read.readlines()
#             for i,v in enumerate(s):
#                 print(i,"번",v)
#             sujeong=int(input("수정할 번호를 입력하세요:"))
#             s[sujeong]=input("수정할 내용:")
#             profile_read.close()

#             profile_write = open(path,'w')
#             for i in s:
#                 profile_write.write(i)
#             profile_write.close()
#         else:
#             print("회원 정보가 없습니다.")
        
#         os.system('pause')
#     elif n== '4':
#         print("프로그램 종료")
#         break
#     else : 
#         print("잘못입력하셨습니다.")
    
    # vsum 함수를 만들어 인자로 전달된 모든 값을 더하는 함수를 만드시오. 
    # 사용예시)vsum(1,2) 결과값 : 3
    #         vsum(1,2,3) 결과값 :6
    #         vsum(1,2,3,4,5) 결과값:15
