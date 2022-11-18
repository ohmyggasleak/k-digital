# #예외처리
# try :
#     n1 = int(input("수 입력: "))
#     n2 = int(input("수 입력: "))


#     s = n1/n2
#     print("결과 : ", s)
# except ZeroDivisionError: #0을 나눌때 오류만 처리
#     print("문제 발생")

# except ValueError: #value 값 오류만 처리
#     print("문제 발생 수 입력")
# print("다음 문장")

# while True:
#     try:
#         num=int(input("수입력(종료 0): "))
#     except: #다른 값들 구분없이 모두 except 처리
#         num = "잘 못 입력. 다시..."
#         # print("잘 못 입력. 다시...")
#         # continue
#     if num == 0 :
#         break
#     print("입력 한 수 : ", num)
# print("다음 문장들 실행~~~~~~~")


# try :
#     n = int(input('수: '))
#     print("입력 한 값 :".n)
# except :
#     print('except 실행')
# else:
#     print('else 실행')
# print("다음 문장들 실행~~~~~~~")


# try :
#     n1 = int(input('수: '))
#     n2 = int(input('수: '))
#     s = n1 / n2
# except :
#     print('except 실행')
# else: #굳이 else 안써도됨 가독성높이기 위해 쓴거임
#     print(f'{n1} / {n2} = {s}')
# finally : #무조건 실행됨 , 마지막에 꼭 결과처리를 해야만 할 때 사용
#     print("finally 실행~~")
# print("다음 문장들 실행~~~~~~~")



# def test():
#     file = 0 
#     try :
#         file = open("c:/aaa1111.txt","r")
#     except : 
#         print("파일이 존재하지 않습니다.")
#     else : 
#         print(file.read())
#     finally:
#         if file:
#             file.close()
#     print("이어서 진행")

#     try :
#         n = input("수 입력: ")
#         if n == '1'  :
#             return 111
#         elif n == '2' :
#             return 222
#     except:
#         pass
#     finally: #return 받아도 마지막으로 실행됨
#         print("test 함수 실행")
#         print("이 코드는 무조건 실행 되어야 합니다.")
#     print("+++++++++++test 함수 종료++++++++++++++++")
# re = test()
# print("결과 : " ,re)

# #강제 예외 (잘 쓸거같지는 않다고함,참고용)
# try : 
#     age = int(input("나이 입력: "))
#     # print("당신의 나이는 :", age-1)

#     if age<0:
#         # raise # raise 발생하면 바로 except로 넘어감
#         # raise ValueError() #이러면 ValueError로 넘어감 
#         raise Exception("000000안됨")
# except ValueError:
#     print("문자는 입력할 수 없음..")
# except Exception as e:
#     print("0살 아래 안됨!!..")
#     print(e)
# except : #모든 값을 처리하는  except는 제일 아래에 써서 처리해야함
#     print("0살 아래의 나이는 없음..")
# else: 
#     print("당신의 나이는 :",age-1)

# #주민번호 앞자리 입력 프로그램
# while True:
#     try:
#         personal_num = int(input("주민번호 앞 자리 입력(예 900402): "))
#         if personal_num > 900000:
#             print('가입불가')
#         elif len(str(personal_num)) != 6:
#             print("길이가 이상합니다.")
#     except ValueError :
#         print("잘못입력하셨습니다. 숫자만 입력해주세요.")
  