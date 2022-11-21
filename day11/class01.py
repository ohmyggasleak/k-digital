'''
클래스 변수 : 클래스가 실행될 때 생성
 - 프로그램 내에서 접근 가능
인스턴스(객체) 변수 : 객체가 생성될 때 생성
 - 객체를 이용해서만 접근 가능
지역변수 : 특정 지역이 실행될 때 생성
 - 특정지역에서만 접근 가능
'''
# class Variable01:
#     def var(self):
#         v = 100
#         print("var v: ",v)
#         # return v 
#     def var02(self,v):
#         print("20 v: ", v)
# vv = Variable01()
# vv.var()
# # v.var02() #v->는 찾을수 없음 vv로해야함
# v = vv.var()
# vv.var02(v)

# print("-"*10)

# class Var02 : 
#     def var(self):
#         self.v = 100  # 해당하는 클래스 내부에서 사용가능한 변수(인스턴스 변수)
#         print("var : " , self.v)
#     def var02(self):
#         print("20 v : ", self.v)

# vv = Var02()
# vv.var()
# vv.var02()

# print("-"*10)
# class Student:
#     def inputSt(self):
#         self.name = input("이름 입력 : ")
#         self.age = input("나이 입력: ")
#     def printSt(self):
#         print(self.name,"님")
#         print(self.age,"살")

# s = Student()
# s.inputSt()
# s.printSt()


# class Score:
#     def inputSt(self):
#         self.name = input("이름 : ")
#         self.kor = int(input("국어 점수: "))
#         self.eng = int(input("영어 점수: "))
#         self.math = int(input("수학 점수: "))

#     def sum_(self):
#         self.sum = self.kor + self.eng + self.math
#     def avg_(self):
#         self.avg = self.sum / 3
#     def grade_(self):
#         if self.avg>=90:
#             self.grade = 'A'
#         elif self.avg>=80:
#             self.grade = 'B'
#         elif self.avg >= 70:
#             self.grade = 'C'
#         else:
#             self.grade = 'F'
#     def printSt(self):
#         print("합 : {}".format(self.sum))
#         print("평균 : {}".format(self.avg))
#         print("등급: {}".format(self.grade))

# s=Score()
# s.inputSt()
# s.sum_()
# s.avg_()
# s.grade_()
# s.printSt()






