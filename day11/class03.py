'''
상속
- 이미 만들어진 코드를 상속 받는것
- 상속받으면 상속받은 코드를 사용할 수 있다.
'''
# class Calc : 
#     def calc(self):
#         print("부모 나는 계산기야~")
# # c=Calc()
# # c.calc()

# class Computer(Calc) : #상속받고 싶은 클래스를 ()괄호 안에 넣어줌
#     def calc(self):
#         print("자식 나는 계산기야~")
#     def computer(self):
#         print("computer")
#         self.calc() #우선순위가 먼저 자기 클래스안에 있는 (자식)클래스가 우선이고 없으면 부모클래스가 실행 : 오버라이징이라고 불림
#         super().calc() #super()를 사용하면 부모 클래스를 먼저 찾아감
# c = Computer()
# c.computer()
# c.calc()

# print("-"*10)
# class MemberInfo:
#     def inputMember(self,m):
#         while True:
#             self.name = input("이름 입력 : ")
#             if m.get(self.name) != None:
#                 print("아이디 있음")
#                 continue
#             break
#         self.age = input("나이 입력 : ")
#         self.addr = input("주소 입력 : ")

# class Display:
#     def display(self):
#         mem_dic = {}
#         for i in range(3):
#             self.mem = MemberInfo()
#             self.mem.inputMember( mem_dic )
            
#             mem_dic[self.mem.name] = self.mem
        
#         print("--- 내용 출력 ---")
#         # for k,v in mem_dic.items():
#         #     print(k,":",v)
#             # print(v.name)
#             # print(v.age)
#             # print(v.addr)
#             # print("----")
#         print(mem_dic)
#         print(mem_dic[self.mem.name])
#         print(mem_dic[self.mem.name].name)
#         print(mem_dic[self.mem.name].age)
#         print(mem_dic[self.mem.name].addr)
# d = Display()
# d.display()


# ##  T  ####
# print("-"*10)
# class MemberInfo:
#     def inputMember(self):
#         self.name = input("이름 입력 : ")
#         self.age = input("나이 입력 : ")
#         self.addr = input("주소 입력 : ")
#     def __str__(self):
#         return f"이름[{self.name}]\n나이[{self.age}]"
# class Display:
#     def display(self):
#         mem_dic = {}
        
#         for i in range(3):
#             self.mem = MemberInfo()
#             self.mem.inputMember()
#             #print( self.mem.name )
#             mem_dic[self.mem.name] = self.mem
#         print("--- 내용 출력 ---")
        
#         for k, v in mem_dic.items():
#             print( v )
#             #print(k,":", v.age)
#             #print(k,":",v.name)
#             #print(k,":",v.age)
#             #print(k,":",v.addr)
#             print("-----")
#         #print( mem_dic )
#         #print( mem_dic[self.mem.name] )
#         #print( mem_dic[self.mem.name].name )
#         #print( mem_dic[self.mem.name].age )
#         #print( mem_dic[self.mem.name].addr )
# d = Display()
# d.display()



# class MemberInfo:
#     def inputMember(self):
#         self.name = input("이름 입력 : ")
#         self.age = input("나이 입력 : ")
#         self.addr = input("주소 입력 : ")

# class Display:
#     def display(self):
#         mem_dic = {}
#         self.mem = MemberInfo()
#         self.mem.inputMember()
            
#         mem_dic[self.mem.name] = self.mem
        
#         print("--- 내용 출력 ---")
#         # for k,v in mem_dic.items():
#         #     print(k,":",v)
#             # print(v.name)
#             # print(v.age)
#             # print(v.addr)
#             # print("----")
#         print(mem_dic)
#         print(mem_dic[self.mem.name])
#         print(mem_dic[self.mem.name].name)
#         print(mem_dic[self.mem.name].age)
#         print(mem_dic[self.mem.name].addr)
# d = Display()
# d.display()


class Member:
    def inputMember(self):
        self.name = input("이름입력 : ")
        self.id=input("아이디 입력 : ")
        self.pw=input("비밀번호 입력 : ")
        
#     def login(self):
#         id_ = input("인증할 아이디 입력 : ")
#         pw_ = input("인증할 비밀번호 입력 :")
#         if self.id == id_ and self.pw ==pw_:
#             print("인증 통과")
#         elif self.id != id_:
#             print("존재하지 않은 아이디입니다.")
#         elif self.pw != pw_:
#             print("비밀번호 틀림")
#     def displayMembers(self):
#         print("{:=^19}".format("모든 사용자 보기"))
#         print(f"이름 : {self.name}")
#         print(f"아이디 : {self.id}")
#         print(f"비밀번호 : {self.pw}")
class Display:
    def display(self):
        mem=Member()
        mem.inputMember()
        info[mem.id]=self.mem
        

info = {}

while True:
    print("1.로그인\n2.회원가입\n3.모든 사용자 보기\n4.종료")
    n=input(">>>>")
    if n == '1':
        mem.login()
    elif n == '2':
        mem = Member()
        mem.inputMember()
        
    elif n== '3':
        mem.displayMembers()
    elif n== '4':
        break
    else:
        print("다시입력하시오")

