'''
class
- 틀. 틀안에 모든 기능과 변수가 존재한다.
- 하나의 자료형이다.

객체
- 클래스 자료형으로 변수를 만들면 객체라고 표현한다.

메소드
- 클래스 안에 함수를 만들면 메소드라 한다.

절차지향 보다 객체지향이 더 무겁고 처리속도가 느림 (하지만 객체지향이 더 편리함)

절차 지향은 틀 없이 따로따로 기능별로 

객체 지향은 틀 안에 여러가지 기능포함
'''

# class Info :  # Info의 첫글자는 대문자
#     name = None
#     add = None
#     age = None
#     stNum = None
#     phNum = None

# i = Info()
# i.name='홍길동'   #'.' : 멤버접근연산자를 의미(Info를 찾아가 내용들을 확인한다는느낌)
# i.age = 20
# i.addr = '산골짜기'

# print(i.name, i.age, i.addr)

# def test():
#     info = Info()
#     info.name = '테스트'
#     print(info.name)

# def test1():
#     info =  Info()
#     info.name = '연습중'
#     print(info.name)

# test()
# test1()

# class MyClass :
#     name = None
#     def test(self):
#         print("test 메소드입니다.")
#         print(self)
#         print('-'*20)


# c = MyClass()
# c.test()
# print(c)

# class MethodTest01:
#     def sumFunc(self):
#         n1 = int(input('수 입력: '))
#         n2 = int(input('수 입력: '))
#         s = n1 + n2
#         print("합: ",s)
#     def myInput(self):
#         n1 = int(input('수 입력: '))
#         n2 = int(input('수 입력: '))
#         return n1, n2
#     def sumN(self, n1, n2):
#         return n1+n2
#     def myPrint(self,*t):
#         print(f"{t[0]}+{t[1]}={t[2]}")

# obj = MethodTest01()
# # obj.sumFunc()
# # tul = obj.myInput()
# # print(tul)
# n1 , n2 = obj.myInput()
# s = obj.sumN(n1,n2)
# obj.myPrint(n1,n2,s)


