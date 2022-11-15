'''
딕셔너리
- key와 value 하나의 쌍으로 이루어져 있다.
- 탐색 속도가 빠르며 사용하기 편리하다
- 중괄호로 묶여 있으며 키와 값의 쌍으로 이루어져 있다.
'''

# dic = {"이름":"홍길동","전화번호":"010-7878","주소":"산골짜기"}
# print(dic)
# print(type(dic))

# mobile = {"품명":"겔럭시","가격":1000}
# print(mobile)
# print(mobile['품명'])

# impo = {}
# impo['파이썬']="www.pyhton.org"
# impo['네이버']="www.naver.com"
# print(impo)
# print(impo['파이썬'])
# print(impo['네이버'])

# impo = {}
# impo[input("등록할 키 입력:")]=input("등록할 값 입력:")
# print(impo)
# print(impo.keys())

# num={1:"일",2:"이",3:"삼"}
# print(num.keys())
# print(num.values())

# print(type(num.keys()))
# li = list(num.keys())
# print(li, li[0])
# for i in num.keys():
#     print(i,':',num[i])

# num={1:"일",2:"이",3:"삼"}
# print(num[1])
# print(num.get(1))

# # print(num[111])
# print(num.get(111)) # 111값이 없으면 None 출력

# key = int(input("key 입력: "))
# result = num.get(key)
# if result == None:
#     print("찾는 내용이 없습니다.")
# else:
#     print(key,":",num[key])

# dic = {}
# while True:
#     print("1.메뉴등록\n2.메뉴별 가격 보기\n3.가격수정\n4.종료")
#     n = input(">>>")
#     if n == '1' :
#         menu=input("메뉴 입력: ")        
#         if dic.get(menu)==None:
#             price=int(input("가격 입력: "))
#             dic[menu]=price
#             print("메뉴가 등록되었습니다.")
#         else:
#             print("이미 등록 되어 있습니다.")
#     elif n == '2' :
#         for i in dic.keys():
#             print(i,':',("{:,}원").format(dic[i]))
#     elif n == '3':
#         menu = input("가격을 수정할 목록을 입력하세요 :")
#         if dic.get(menu)==None:
#             print("등록을 먼저 진행하거나 메뉴를 확인해 주십시오.")
#         else:
#             dic[menu]=int(input("수정가격: "))
#     elif n == '4':
#         print("프로그램이 종료됩니다.")
#         break
#     else:
#         print("잘 못 입력하셨습니다.")


# st = {"학번":1234, "이름":"홍길동"}
# print(st)
# print(st.items())
# for k,v in st.items():
#     print(f"{k}:{v}")
    
# print(st.setdefault("학번",5555)) # 학번이라는 key가 있으면 추가하지 않음
# print(st.setdefault("학번1",5555)) # 학번1이라는 key가 없어서 5555추가
# print(st)

# ls = [10,{"key":"value"},30]
# print(ls[0])
# print(ls[1], ls[1]['key'])
# print(ls[2])

# dic={'li':[10,20,30],"k":"value"}
# print(dic['li'][2])
# print(dic['k'])

# info = {}
# info02 = {}
# info02['가수'] = '개가수'
# info02['인원수'] = 3
# info02['노래'] = '신나리'
# # info[info02['가수']] = info02 # 얕은복사
# info[info02['가수']] = info02.copy() #깊은복사
# print(info02)
# print(info)

# # for k,v in info.items():
# #     # print(k)
# #     # print(v)
# #     for kk,vv in v.items():
# #         print(kk,":",vv)

# info02['안녕']='하세요'
# print('-'*10)
# print(info)
# print(info02)

# # 초기화
# info = {}
# info.clear() 





