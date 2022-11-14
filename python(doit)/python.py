# f = open("파일 읽고 쓰기.py",'w')
# f.close()

#파일 객체 = open(파일 이름, 파일 열기 모드)
#r = 읽기모드 - 파일을 읽기만 할 때 사용
#w = 쓰기모드 - 파일에 내용을 쓸 때 사용
#a = 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용

# # 원하는 곳에 파일 생성
# f= open("E:/김진성.k-디지털/python-workspace/day4/새파일.txt",'w')
# f. close()

# # writedata.py
# f = open("새파일.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# #readline
# # readline_test.py
# f = open("새파일.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

# # readline_all.py
# f = open("새파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# #readlines 함수 사용
# f = open("새파일.txt","r")
# lines = f.readlines()
# for line in lines:
#     line=line.strip() #줄 끝의 줄 바꿈 문자 제거
#     print(line)
# f.close()

# #read 함수 사용
# #f.read() 는 파일의 내용 전체를 문자열로 돌려준다. 따라서 위 예의 data는 파일의 전체내용이다.
# f= open("새파일.txt",'r')
# data = f.read()
# print(data)
# f.close()

'''
쓰기 모드('w')로 파일을 열 때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 된다. 
하지만 원래 있던 값을 유지하면서 단지 새로운 값만 추가해야 할 경우도 있다.
이런 경우에는 파일을 추가 모드('a')로 열면 된다.
'''
# # adddata.py
# f = open("새파일.txt",'a')
# for i in range(11, 20):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()
# #추가된 거 확인
# f=open("새파일.txt",'r')
# data = f.read()
# print(data)
# f.close()

# #with문 과 함께 사용하기
# with open("foo.txt","w") as f :
#     f.write("Life is too short, you need python")
# #with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close 됨.

# #sys 모듈로 매개변수 주기
# import sys

# args = sys.argv[1:]
# for i in args:
#     print(i.upper(),end=' ')