'''
tuple
- 중복을 허용하지 않는다.
- 데이터의 변경이 불가능하다.
- index 접근 가능하다
- (소괄호) 표현한다.
'''
# tp = (10,20,30)
# print(tp)
# print(type(tp))
# print(tp[0])
# print(len(tp))
# # tp[0] = 1234 #불가

# tp = (10)
# print(tp,":",type(tp)) #int
# tp = (10,)
# print(tp,":",type(tp)) #tuple
# tp = 10,
# print(tp,":",type(tp)) #tuple

# '''
# 패킹 : 압축(여러개의 값을 하나의 공간에 저장)
# 언패킹 : 하나의 덩어리를 여러개의 공간에 저장
# '''
# tp = 1,2,"패킹",3,4,5
# print("패킹",tp)
# a,b,c,d,e,f = tp
# print(a,b,c,d,e,f) #언패킹

# a,b,*c = tp # *:전체값
# print(a,b,c)
# print(type(c))

# tp = 100, 200 ,300 , 100
# print(tp.index(200))
# print(tp.count(100))



