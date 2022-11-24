'''
class
- 틀 안에 모든 기능과 변수 존재
- 하나의 자료형
객체
- 클래스 자료형으로 만든 변수
메소드
- 클래스안의 함수
'''
'''
- 객체지향 : class 형태, 편리, 속도느리고 무겁  ex. java, python, c++
- 절차지향 : class(틀)없이 따로 존재           ex. c
'''

# 클래스 생성
class Info:
    name = None
    age = None
    id = None
user = Info()   # user : 객체 생성
user.name = '홍길동'
user.age = 20 
user.id = 'aaa'
print(user.name, user.age, user.id)

# 함수에서 class 사용
def test():
    student = Info()    # student : 객체
    student.name = '김개똥' # 객체로 변수에 접근
    print(student.name)
test()  # 김개똥

"""
1. 메소드에 (self)가 있으면 객체 생성을 통해 접근
2. 메소드가 ()이면 객체 접근 불가!, class자체로 접근 가능

class myClass:
    1. def test1():
        pass
    2. def test2(self):
        pass
1. myClass.test1()
2. t = myClass()
   t.test2()
"""

""" 예제와 연습퀴즈 주석으로 묶음~~~
# ex 1 ) 두 수 입력받아서 합 출력 (3가지 함수정의하기!)
class methodTest:
    def myInput(self):  # 입력받는 함수
        n1=int(input('수 입력 :'))
        n2=int(input('수 입력 :'))
        return n1, n2
    def numSum(self, n1,n2):   # 덧셈하는 함수
        return n1+n2
    def sumDisplay(self, *t):  # 결과 출력 함수
        print(f'{t[0]} + {t[1]} = {t[2]}')
obj = methodTest()
num1, num2 = obj.myInput()
sum_ = obj.numSum(num1, num2)
obj.sumDisplay(num1, num2, sum_)

# quiz 1) 입력,출력,연산메소드 만들기
# 1. 두 수를 입력 받아 큰 수 출력하는 class
# 2. 입력받은 수가 짝/홀수 판별하는 class
# 3. 입력받은 수가 3의배수인지 아닌지 판별하는 class
# 4. 수를 입력 받아 소수인지 아닌지 판별하는 class
# 5. 수를 입력 받아 절대값으로만 출력되는 class

class quiz():
    def myInput(self):  # 입력받는 메소드
        num=int(input('수 입력 : '))
        return num
    def maxNum(self, *n): # 큰 수 판별 메소드
        if n[0]>n[1]:
            return n[0]
        else:
            return n[1]
    def display(self, x):   # 출력 메소드
        print('-->', x)
    def evenOdd(self, n):     # 짝/홀 판별 메소드
        if n % 2 == 0:
            return 'even'
        else:
            return 'odd'
    def multiThree(self, n):   # 3의배수 판별 메소드
        if n % 3 == 0:
            return '3의 배수 입니다.'
        else:
            return '3의 배수가 아닙니다.'
    def primeNum(self, n):     # 소수 판별 메소드
        cnt = 0
        for i in range(1, n+1):
            if n % i == 0:
                cnt += 1
        if cnt == 2:
            return '소수입니다.'
        else:
            return '소수가 아닙니다.'
    def absNum(self, n):       # 절댓값 출력 메소드
        if n < 0:
            return -n
        else:
            return n

# 1. 
print('====큰 수 출력====')
ans1 = quiz()
n1 = ans1.myInput()
n2 = ans1.myInput()
maxNum = ans1.maxNum(n1, n2)
ans1.display(maxNum)

# 2.
print('====짝/홀 판별====')
ans2 = quiz()
n = ans2.myInput()
print(ans2.evenOdd(n))

# 3.
print('====3의배수 판별====')
ans3 = quiz()
n = ans3.myInput()
print(ans3.multiThree(n))

# 4.
print('====소수 판별====')
ans4 = quiz()
n = ans4.myInput()
print(ans4.primeNum(n))

# 5.
print('====절댓값 출력====')
ans5 = quiz()
n = ans5.myInput()
abs = ans5.absNum(n)
ans5.display(abs)
"""

'''
클래스 변수     : 클래스가 실행될 때 생성   , 프로그램 내에서 접근 가능
인스턴스 변수   : 객체가 생성될 때 생성     , 객체 이용해서만 접근 가능 , self.~
지역 변수       : 특정 지역이 실행될 때 생성, 특정 지역에서만 접근 가능
'''
class myClass:      # self : 인스턴스 변수, 자기자신의 정보를 알고 있음.
    aaa = '안녕하세요'  # aaa : class 변수 
    def test(self):     # test : 메소드
        print('test')
        print(self.aaa)     # self.aaa : 인스턴스 변수 -> 객체통해 접근
        self.aaa='잘가'     # 인스턴스 변수만 변경됨. class변수 aaa 자체는 변경 X
        print(self.aaa)     # 인스턴스 변수 -> '잘가'
        print(myClass.aaa)  # myClass.aaa : class 변수 -> '안녕하세요'
        print(self.bbb)     # 인스턴스 변수 bbb를 객체통해서 지정

myClass.ccc = '클래스 변수' # class로 접근 가능!
print(myClass.ccc)
print(myClass.aaa)  # myClass.aaa : class 변수 -> 객체없이 접근 가능!

c = myClass()   # c : 객체
c.bbb='인스턴스 변수'   # 인스턴스 변수는 객체 통해서만! bbb 지정

c.test()        # 객체로 메소드에 접근, test(self)는 객체(c)가 생성될때 생성

## self 생략 가능
class omitSelf:
    def test():         # class 접근 O / 객체 접근 X
        print('self 없음')
    def testSelf(self): # 객체 접근 O / class 접근 X
        print('self 있음')
omitSelf.test()     # class 메소드 접근 O
#omitSelf.testSelf()    : error

mySelf=omitSelf()   # 객체 생성과 함께 testSelf(self) 메소드가 생성됨.
mySelf.testSelf()   # 객체통한 접근
#mySelf.test()          : error

"""# quiz
# 인스턴스 변수 : name, grade, kor, eng, math, sum, avg
# class에서 입력, 출력, 합, 평균, 등급 구하는 메소드 구현 
print('-'*20)
class Student02:
    def inputSt(self):
        self.name=input('이름 입력 : ')
        self.kor=int(input('국어점수 입력 : '))
        self.eng=int(input('영어점수 입력 : '))
        self.math=int(input('수학점수 입력 : '))
    def sumSt(self):
        self.sum = self.kor + self.eng + self.math
    def avgSt(self):
        self.avg = round(self.sum / 3, 2)
    def gradeSt(self):
        if self.avg >= 90:
            self.grade = 'A'
        elif self.avg >= 80:
            self.grade = 'B'
        elif self.avg >= 70:
            self.grade = 'C'
        else:
            self.grade = 'F'
    def outputSt(self):
        print("이름 : " , self.name )
        print( f"국 : {self.kor}, 영 : {self.eng}, 수 : {self.math}" )
        print("합계 : " , self.sum )
        print("평균 : " , self.avg )
        print("등급 : " , self.grade )
ss = Student02()
ss.inputSt()
ss.sumSt()
ss.avgSt()
ss.gradeSt()
ss.outputSt()
"""

'''
생성자
- 객체가 만들어질 때 자동으로 호출되는 메소드
- __init__(self) : 변수 초기화 목적으로 사용
- __str__(self) : 객체 정보를 원하는 값으로 표현
                ex ) 객체(self) 정보 : <__main__.TestClass03 object at 0x000001C580A9AE50>
                    -> return (f'{self.a}, {self.b}')
'''
class TestClass:
    def __init__(self, version, memory):
        self.version = version
        self.memory = memory
    def __str__(self):
        return (f'{self.version}, {self.memory}')
t = TestClass('win10', '8GB')   # 초기화 변수 넣음
print(t)    # 출력값 : <__main__.TestClass object at 0x000001FC8F838DD0> 
            #     ==>  win10, 8GB

'''
상속
- 이미 만들어진 코드를 상속받는 것
- 상속받으면 상속받은 코드 사용 가능
- 자신의 코드에 있는 메소드의 경우, 자신우선 실행!
'''
class system:
    def note(self):
        print('부모 나는 메모장이야~')
    def calc(self):
        print('부모 나는 계산기야~')

class myCalc(system):   # system을 상속받음!
    def calc(self):
        print('자식 나는 계산기야~')
    def computer(self):
        print('computer')
        self.note()     # 상속 메모장
        self.calc()     # 자식 계산기
        super().calc()  # 부모 계산기

m = myCalc()
m.computer()

# 정보 입력 받아서 저장
# 입력받는 class, 정보 저장하는 class 생성하기
class myInput:
    def inputSimple(self):
        self.name = input('이름 입력 : ')
        self.age = int(input('나이 입력 : '))
        self.addr = input('주소 입력 : ')

    def inputMember(self, dic): # 중복 해결 : 동일 이름 입력 시 -> '동일한 이름이 있습니다. 다시'
        while True:
            self.name = input('이름 입력 : ')
            if dic.get(self.name) != None:
                print('동일한 이름이 있습니다. 다시')
                continue
            break
        self.age = int(input('나이 입력 : '))
        self.addr = input('주소 입력 : ')
    

class oneMemory(myInput):   # input 1회 받아서 dict 추가
    def oneMemory(self):    # 객체 생성하는 경우
        self.user = myInput()   # self.user : 인스턴스 객체 생성
        self.user.inputSimple() # 객체로 기능 실행
        memory[self.user.name]=self.user
        print(memory)
        print(memory[self.user.name])
        print(memory[self.user.name].age)
        print(memory[self.user.name].addr)
        print(memory[self.user.name].name)
    
    # 깊은 복사 필요없을 경우 객체 추가 생성 없이 바로 접근 가능
    def oneMemory02(self):  # 객체 생성 없는 경우
        self.inputSimple()  # 객체없이 상속 class로 기능실행
        memory[self.name]=self
        print(memory)
        print(memory[self.name])
        print(memory[self.name].age)
        print(memory[self.name].addr)
        print(memory[self.name].name)

import copy
class myMemory(myInput):    # input 여러번(num번) 받아서 dict 추가
    def addMemory(self):
        num=int(input('명 수 입력 : '))
        for i in range(num):
            self.user = myInput()   # 인스턴스 객체 생성
            self.user.inputMember(memory) # 객체로 기능 실행
            memory[self.user.name] = self.user
            print(self)         # self 는 동일
            print(self.user)    # self.user 는 입력마다 달라짐.
            print(memory[self.user.name])   # 위의 self.user와 동일 --> 얕은 복사 (self.user와 memory[self.user.name]은 같은 메모리 공간을 쓰고 있음!)
                                            #                        : self.user 변형하면 memory[self.user.name]도 변형됨. 
                                            #                          따라서 반복할때마다(self.user값의 input이 바뀔때마다) 새롭게 객체 생성해줘야함!
        print('이름\t나이\t주소')
        for k, v in memory.items():
            print(k, '\t', v.age, '\t', v.addr)

    def deepcopyMemory(self):   # 깊은 복사 + import copy
        num=int(input('명 수 입력 : '))
        self.user = myInput()   # 객체 생성 한번!
        for i in range(num):
            self.user.inputMember(memory) # 객체로 기능 실행
            memory[self.user.name]=copy.deepcopy(self.user) # deepcopy 실행!
            print(self)                     # self  동일
            print(self.user)                # self.user 동일
            print(memory[self.user.name])   # 입력마다 다르게 생성 --> 깊은 복사 (data만 삭제해서 새로운 주소값(메모리 공간)인 memory[self.user.name]에 카피해줌.)
        print('이름\t나이\t주소')
        for k, v in memory.items():
            print(k, '\t', v.age, '\t', v.addr)

memory={}
mm = myMemory()
mm.addMemory()
dm = myMemory()
dm.deepcopyMemory()



## quiz -로그인 프로그램 (더 좋은 코드 : 은아 2)

# 은아 1 - '은아 2'에서 활용도가 좋게 기능을 class 별로 나눠봤어요. 
# 은아 2 -하나의 class에 여러 기능 생성! (input, singup, signin, output 모든 함수를 넣어둠.)
#       - 한개 class로 모두 해결 가능, 하지만 나중에 다른 곳에서 input기능을 쓰고 싶을 때 꺼내서 쓸 수가 없음!!!!!
# 쌤 - class를 여러개 생성(class하나에 기능 하나정도씩만!)
#    - input하는 class하나, signin하는 class하나를 선언하심 -> input하는 class를 다른 곳에서도 끌어다가 활용할 수 있음.


## 은아 1 -활용도가 좋게 기능을 class 별로 나눠봤어요.(input, output, sign)
class myInput:
    def inputMember(self, dic):
        self.name=input('이름 입력 : ')
        while True:
            self.id=input('아이디 입력 : ') # key로 지정 --> 중복 유무 판단 기준
            if dic.get(self.id) != None:
                print('이미 존재하는 아이디입니다. 다시 입력')
                continue
            break
        self.pw=input('비밀번호 입력 : ')
class myOutput:
    def displayAll(self):
        print('=== 모든 사용자 보기 ===')
        for k, v in member.items():
            print('이름 :', v.name)
            print('아이디 :', k)
            print('비밀번호 :', v.pw)
            print('-'*20)
class mySign(myInput, myOutput):
    def signUp(self):
        self.user = myInput()
        self.user.inputMember(member)
        member[self.user.id]=self.user
        print('회원 가입을 축하 합니다.')

    def singIn(self):
        self.userid=input('인증할 아이디 입력 : ')
        self.userpw=input('인증할 비밀번호 입력 : ')
        # dict : member = {k: id, v: self.user(v.name, v.id, v.pw)}
        if member.get(self.userid) == None:
            print('존재하지 않는 아이디 입니다.')
        else:
            if member[self.userid].pw != self.userpw:
                print('비밀번호 틀림')
            else:
                print('인증 통과')

cc = mySign()
member={}   # k:self.id, v:self.pw
while True:
    print('1. 로그인 2. 회원가입 3. 모든 사용자 보기 4. 종료', end='')
    option = input('>>> : ')
    if option == '1':   # 로그인, 인증할 아이디 입력, 비번 입력, 
        cc.singIn()
    elif option == '2': # 회원가입, 아이디 입력, 비번 입력, dict추가하기
        cc.signUp()
    elif option == '3':
        cc.displayAll()
    elif option == '4':
        break


## 은아 2 -하나의 class에 여러 기능 생성! (input, singup, signin, output 모든 함수를 넣어둠.)
class computer02:
    member={}   # k:self.id, v:self.pw

    def inputMember(self):
        self.name=input('이름 입력 : ')
        self.id=input('아이디 입력 : ') # key로 지정
        self.pw=input('비밀번호 입력 : ')

    def signUp(self):
        self.user = computer02()
        self.user.inputMember()
        computer02.member[self.user.id]=self.user
        print('회원 가입을 축하 합니다.')

    def singIn(self):
        self.userid=input('인증할 아이디 입력 : ')
        self.userpw=input('인증할 비밀번호 입력 : ')
        # dict : computer02.member = {k: id, v: self.user(v.name, v.id, v.pw)}
        if computer02.member.get(self.userid) == None:
            print('존재하지 않는 아이디 입니다.')
        else:
            if computer02.member[self.userid].pw != self.userpw:
                print('비밀번호 틀림')
            else:
                print('인증 통과')

    def displayAll(self):
        print('=== 모든 사용자 보기 ===')
        for k, v in computer02.member.items():
            print('이름 :', v.name)
            print('아이디 :', k)
            print('비밀번호 :', v.pw)
            print('-'*20)

cc = computer02()
while True:
    print('1. 로그인 2. 회원가입 3. 모든 사용자 보기 4. 종료', end='')
    option = input('>>> : ')
    if option == '1':   # 로그인, 인증할 아이디 입력, 비번 입력, 
        cc.singIn()
    elif option == '2': # 회원가입, 아이디 입력, 비번 입력, dict추가하기
        cc.signUp()
    elif option == '3':
        cc.displayAll()
    elif option == '4':
        break


## 쌤 - class를 2개 생성(중복 거르는 input, id/pw chk), 나머지 input&output은 다 main문에서 함.
class Member:
    def inputMember(self , info={}):
        self.name = input( "이름 입력 : " )
        while True: # id 중복 처리
            self.id = input( "아이디 입력 : " )
            if info.get( self.id ) != None:
                print( "동일한 아이디. 다시 입력" )
            else: break
        self.pwd = input( "비밀번호 입력 : " )
class Login():
    def userChk(self , info , userId , userPwd ):
        if info.get(userId) != None:
            if info.get(userId).pwd == userPwd:
                return 0    # 인증통과
            else: return 1  # 비밀번호 틀림
        return -1           # 존재하지 않는 아이디 입니다.

info = {}
login = Login()
while True:
    num = input("1.로그인 2.회원가입 3.모든 사용자 보기 4.종료 >>> :")
    if num == '1':
        userId = input("인증할 아이디 입력 : ")
        userPwd = input("인증할 비밀번호 입력 : ")
        result = login.userChk( info , userId , userPwd)
        if result == 0:
            print( '인증 통과' )
        elif result == 1:
            print( "비밀번호 틀림" )
        else:
            print( "존재하지 않는 아이디 입니다" )
    elif num == '2' :
        mem = Member()
        mem.inputMember( info )
        info[mem.id] = mem
        print( "회원 가입을 축하 합니다" )
    elif num == '3':
        print("=== 모든 사용자 보기 ===")
        for k , v in info.items():
            print("이름 : " , v.name)
            print("아이디 : " , v.id)
            print("비밀번호 : " , v.pwd)
            print( "-" * 15 )
    elif num == '4':
        break


## quiz -상속문제 (더 좋은 코드 : 1. 은아)
# !1. 은아 : class 세분화 수정 후
# 2. 은아 : class 세분화 수정 전
# 3. 쌤 :

# 1. 은아 : class 세분화 수정 후
import os
class Computer:
    def __init__(self, version={}, function={}):
        self.version = version
        self.function = function

    def printV(self):
        print('사양을 보여 줍니다')
        print('-'*20)
        for k, v in self.version.items():
            print(k, ':', v)
        print('-'*20)

    def printF(self):
        print('기능을 보여 줍니다')
        print('-'*20)
        for k, v in self.function.items():
            print(k, ':', v)
        print('-'*20)
        self.userf = input('사용할 기능 입력 : ')
        os.system(self.function[self.userf])

class myInput:
    def inputMember(self, dic):
        self.name=input('이름 입력 : ')
        while True:
            self.id=input('아이디 입력 : ') # key로 지정 --> 중복 유무 판단 기준
            if dic.get(self.id) != None:
                print('이미 존재하는 아이디입니다. 다시 입력')
                continue
            break
        self.pw=input('비밀번호 입력 : ')

class myOutput:
    def displayAll(self):
        print('=== 모든 사용자 보기 ===')
        for k, v in member.items():
            print('이름 :', v.name)
            print('아이디 :', k)
            print('비밀번호 :', v.pw)
            print('-'*20)

class mySign(myInput, myOutput, Computer):
    def signUp(self):
        self.user = myInput()
        self.user.inputMember(member)
        member[self.user.id]=self.user
        print('회원 가입을 축하 합니다.')

    def singIn(self):
        self.userid=input('인증할 아이디 입력 : ')
        self.userpw=input('인증할 비밀번호 입력 : ')
        # dict : member = {k: id, v: self.user(v.name, v.id, v.pw)}
        if member.get(self.userid) == None:
            print('존재하지 않는 아이디 입니다.')
        else:
            if member[self.userid].pw != self.userpw:
                print('비밀번호 틀림')
            else:
                print('인증 통과')
                return True

version = {'cpu' : 'i7', 'memory': 8}
funtion = {'계산기' : 'calc', '메모장' : 'notepad'}
cc = mySign(version, funtion)   # computer02는 computer를 상속받으므로, computer의 초기화를 conputer02에서 시켜줌
member={}   # k:self.id, v:self.pw
while True:
    print('1. 로그인 2. 회원가입 3. 모든 사용자 보기 4. 종료', end='')
    option = input('>>> : ')
    if option == '1':   # 로그인, 인증할 아이디 입력, 비번 입력, 
        if cc.singIn():
            while True:     # computer class 상속받아서 실행(self.function())
                print('1. version확인\n2. 기능 확인\n3. 종료')
                option = input('>>> : ')
                if option == '1':
                    cc.printV()
                elif option == '2':
                    cc.printF()
                elif option == '3':
                    break
    elif option == '2': # 회원가입, 아이디 입력, 비번 입력, dict추가하기
        cc.signUp()
    elif option == '3':
        cc.displayAll()
    elif option == '4':
        break


# 2. 은아 : class 세분화 수정 전
import os
class Computer:
    def __init__(self, version={}, function={}):
        self.version = version
        self.function = function

    def printV(self):
        print('사양을 보여 줍니다')
        print('-'*20)
        for k, v in self.version.items():
            print(k, ':', v)
        print('-'*20)

    def printF(self):
        print('기능을 보여 줍니다')
        print('-'*20)
        for k, v in self.function.items():
            print(k, ':', v)
        print('-'*20)
        self.userf = input('사용할 기능 입력 : ')
        os.system(self.function[self.userf])

class computer02(Computer):
    member={}   # k:self.id, v:self.pw

    def inputMember(self):
        self.name=input('이름 입력 : ')
        self.id=input('아이디 입력 : ') # key로 지정
        self.pw=input('비밀번호 입력 : ')

    def signUp(self):
        self.user = computer02()
        self.user.inputMember()
        computer02.member[self.user.id]=self.user
        print('회원 가입을 축하 합니다.')

    def singIn(self):
        self.userid=input('인증할 아이디 입력 : ')
        self.userpw=input('인증할 비밀번호 입력 : ')
        # dict : computer02.member = {k: id, v: self.user(v.name, v.id, v.pw)}
        if computer02.member.get(self.userid) == None:
            print('존재하지 않는 아이디 입니다.')
        else:
            if computer02.member[self.userid].pw != self.userpw:
                print('비밀번호 틀림')
            else:
                print('인증 통과')
                return True
                
    def displayAll(self):
        print('=== 모든 사용자 보기 ===')
        for k, v in computer02.member.items():
            print('이름 :', v.name)
            print('아이디 :', k)
            print('비밀번호 :', v.pw)
            print('-'*20)


version = {'cpu' : 'i7', 'memory': 8}
funtion = {'계산기' : 'calc', '메모장' : 'notepad'}
cc = computer02(version, funtion)   # computer02는 computer를 상속받으므로, computer의 초기화를 conputer02에서 시켜줌
while True:
    print('1. 로그인 2. 회원가입 3. 모든 사용자 보기 4. 종료', end='')
    option = input('>>> : ')
    if option == '1':   # 로그인, 인증할 아이디 입력, 비번 입력, 
        if cc.singIn():
            while True:     # computer class 상속받아서 실행(self.function())
                print('1. version확인\n2. 기능 확인\n3. 종료')
                option = input('>>> : ')
                if option == '1':
                    cc.printV()
                elif option == '2':
                    cc.printF()
                elif option == '3':
                    break
    elif option == '2': # 회원가입, 아이디 입력, 비번 입력, dict추가하기
        cc.signUp()
    elif option == '3':
        cc.displayAll()
    elif option == '4':
        break


# 3. 쌤
import os

class Computer:
    def __init__(self , version = {} , function = {} ):
        self.version = version
        self.function = function
    def printVersion(self):
        print( "사양을 보여 줍니다" )
        print("------------------")
        for k, v in self.version.items() :
            print(k,":",v)
        print("------------------")
    def printFunction(self):
        print( "기능을 보여 줍니다" )
        print("------------------")
        for k, v in self.function.items() :
            print(k,":",v)
        print("------------------")
        value = input("사용할 기능 입력 : ")
        os.system(self.function[value])
    def display(self):    
        self.version = {"cpu":'i7' , "memory":'8'}
        self.function = {"계산기":"calc", "메모장":"notepad"}
        while True:
            print("1. version확인")
            print("2. 기능 확인")
            print("3. 종료")
            num = int( input(">>> : ") )
            if num == 1:
                self.printVersion()
            elif num == 2:
                self.printFunction()
            else:
                break
class Member:
    def inputMember(self , info={}):
        self.name = input( "이름 입력 : " )
        while True:
            self.id = input( "아이디 입력 : " )
            if info.get( self.id ) != None:
                print( "동일한 아이디. 다시 입력" )
            else: break
        self.pwd = input( "비밀번호 입력 : " )
class Login( Computer ):
    def userChk(self , info , userId , userPwd ):
        if info.get(userId) != None:
            if info.get(userId).pwd == userPwd:
                return 0
            else: return 1
        return -1

info = {}
login = Login()
while True:
    num = input("1.로그인 2.회원가입 3.모든 사용자 보기 4.종료 >>> :")
    if num == '1':
        userId = input("인증할 아이디 입력 : ")
        userPwd = input("인증할 비밀번호 입력 : ")
        result = login.userChk( info , userId , userPwd)
        if result == 0:
            print( '인증 통과' )
            login.display()     # 상속내용 실행
        elif result == 1:
            print( "비밀번호 틀림" )
        else:
            print( "존재하지 않는 아이디 입니다" )
    elif num == '2' :
        mem = Member()
        mem.inputMember( info )
        info[mem.id] = mem
        print( "회원 가입을 축하 합니다" )
    elif num == '3':
        print("=== 모든 사용자 보기 ===")
        for k , v in info.items():
            print("이름 : " , v.name)
            print("아이디 : " , v.id)
            print("비밀번호 : " , v.pwd)
            print( "-" * 15 )
    elif num == '4':
        break




































