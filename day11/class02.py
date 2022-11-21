# class AAA:
#     def test1(self):
#         print("test1")
#         print(self.num) #self.num으로 받아줘야함
# a = AAA()
# a.num = 12345 #인스턴스 변수로 이용함 (num이랑 위에 self.num이랑 변수이름 맞춰야함)
# a.test1()


#ERROR
# class BBB:
#     aaa = "안녕하세요"
    
#     def test1(self):
#         print("test1")
#         print(aaa)

# b=BBB()
# b.test1()

# #이렇게 써야함
# class BBB:
#     aaa = "안녕하세요"  #클래스 변수 (클래스가 생성되는 동시에 만들어지는 변수)
#     def test1(self):
#         print("test1")
#         print(self.aaa) #객체를 불러올때 만들어지는 변수(self.aaa)
#         print(BBB.aaa)

# b=BBB()
# b.test1()
# print(BBB.aaa)
# BBB.num = "넘입니다" #클래스 변수 선언
# print(BBB.num)

# b=BBB()
# b.bbb = "bbb입니다"
# # print(BBB.bbb) #오류
# print(b.bbb)

# print("-"*10)
# def test():
#     b = BBB()
#     b.test1()
# test()

# print("-"*10)
# class CCC:
#     a = "aaaa"
#     def test():
#         print("test입니다")
#     def test1(self):  #self가만들어지는 시기는 객체가 만들어지고나서 
#         print("test입니다")
# CCC.test()
# # CCC.test1() #오류
# c = CCC() 
# c.test1() #객체를 통해서 test1을 불ㄹ러옴
# # c.test() #오류


'''
생성자
- 객체가 만들어질 때 자동으로 호출되는 메소드
- __init__(self)이름을 사용한다
- 일반적으로 변수 초기화 목적으로 사용한다.
'''
# class TestClass :
#     def __init__(self):
#         print("생성자 실행")
#     def test(self):
#         pass
# t = TestClass()
# t.test()

# class TestClass02:
#     def __init__(self,name):
#         self.name = name
#     def printName(self):
#         print("당신의 이름은: ",self.name)
# n = input("이름 입력: ")
# t =TestClass02(n)
# t.printName()


# class TestClass03:
#     def __init__(self,version,memory):
#         self.version = version
#         self.memory = memory 
#     def printM(self):
#         print("버전 : ",self.version)
#         print("메모리 : ",self.memory)
#     def __str__(self):
#         # return "원하는 값 표현"
#         return f"{self.version},{self.memory}"
# t = TestClass03("win10","8GB")
# t.printM()
# print("t:",t)


# #coumputer 만들기 문제
# import os
# class Computer:
#     def __init__(self,version,function):
#         self.version = version
#         self.function = function

#     def printVersion(self):
#         print("사양을 보여줍니다.")
#         print("-"*15)
#         for j,k in self.version.items() :
#             print(j,':',k)
#         print("-"*15)

#     def skill(self):
#         print("-"*15)
#         print("계산기 : calc \n메모장 : notepad")
#         print("-"*15)
#         s=input("사용할 기능 입력: ")
        
#         os.system(self.function[s])
# version = {'cpu':'i7','mememory':'8'}
# funtion = {'계산기':'calc','메모장':'notepad'}
# com = Computer(version,funtion)
# while True:
#     print("1.version 확인\n2.기능 확인\n3. 종료")
#     n=input(">>>")
    
#     if n=='1':
#         com.printVersion()

#     elif n=='2':
        
#         com.skill()

#     elif n=='3':
#         print("종료")
#         break
#     else:
#         print("잘 못 입력하셨습니다.")


# ###정답
# import os
# class Computer:
#     def __init__(self , version={}, function={} ):
#         self.version = version
#         self.function = function
#     def printVersion(self):
#         print( "사양을 보여 줍니다" )
#         print("------------------")
#         for k, v in self.version.items() :
#             print(k,":",v)
#         print("------------------")
#     def printFunction(self):
#         print( "기능을 보여 줍니다" )
#         print("------------------")
#         for k, v in self.function.items() :
#             print(k,":",v)
#         print("------------------")
#         value = input("사용할 기능 입력 : ")
#         os.system(self.function[value])
        
# version = {"cpu":'i7' , "memory":'8'}
# function = {"계산기":"calc", "메모장":"notepad"}
# com = Computer(version, function)
# while True:
#     print("1. version확인")
#     print("2. 기능 확인")
#     print("3. 종료")
#     num = int( input(">>> : ") )
#     if num == 1:
#         com.printVersion()
#     elif num == 2:
#         com.printFunction()
#     else:
#         break

