# 함수에 고정값 넣기
def sum_func(x1=1, x2=22, x3=100):
    re = x1 + x2 + x3
    return re
re = sum_func(x3=10000)
print("합 : ",re)   #합 :  10023
re = sum_func(10,20,30)
print("합 : ",re)   #합 :  60

print('='*20)

# parameter
def func01( *par ):
    print( type(par) )  #<class 'tuple'>
    for i in par:
        print( i )  #10\n20\n30\n40
func01(10,20,30,40)

print('='*20)

#map
'''
- 리스트의 요소를 지정된 함수로 처리해주는 함수
- map의 기본조건식 = list(map(함수이름, 리스트))
'''

#일반적인 형변환 과정
li = ['100','200','300']
print("변경 전 : ",li)  #변경 전 :  ['100', '200', '300']
for i in range( len(li) ):
    li[i] = str( int(li[i])+10 )    
print("변경 후 : ",li)  #변경 후 :  ['110', '210', '310']

print('='*20)

#map을 이용한 형변환 과정
li = ['100','200','300']
print("변경 전 : ",li)  #변경 전 :  ['100', '200', '300']
li = list(map(int, li) ) 
print("변경 후 : ",li)  #변경 후 :  [100, 200, 300]
for i in range( len(li) ):
    li[i] = str( li[i]+10 ) 
print("변경 후 : ",li)  #변경 후 :  ['110', '210', '310']

print('='*20)

# ex 1 ) def + map
li = ['100','200','300']
def test1( a ):
    return str(int(a)+10)
li = list(map(test1, li)) 
print("함수 : ",li) #함수 :  ['110', '210', '310']

print('='*20)

# ex 2 ) def+map 
def test( num ):
    return str(num)
li = [1,2,3,4]
print("변경 전 : ",li)  #변경 전 :  [1, 2, 3, 4]
li = list(map(test, li))
print("변경 후 : ", li) #변경 후 :  ['1', '2', '3', '4']

print('='*20)

# lambda 
'''
- lambda는 함수를 한 줄로 표현할 수 있는 간편한 방법
- 가독성이 높고, 코드가 간결하다.
- 코드가 간결하면 컴퓨터의 처리속도가 높아진다.
- '익명함수'라고도 불린다.
''' 
# ex 1 ) lambda
def big(a, b):
    if a>b:
        return a
    else:
        return b
result = big(10, 20)
print( result ) #20

bi = lambda a,b : a if(a>b) else b    #위의 def를 lambda형식으로 변환
result = bi(200,1000)
print( result ) #1000

print('='*20)

# ex 2 ) lambda
bi = lambda a : a + 1000
print( bi(100) )    #1100

print('='*20)

# lambda + map
li = ['100','200','300']
lb = lambda x : str( int(x)+1000 )
li = list( map(lb, li) )
#li = list( map(lambda x : str( int(x)+1000 ), li) )
print("lambda : ", li)  #lambda :  ['1100', '1200', '1300']

print('='*20)

# ex 1 ) def -------> lambda
day = { '날짜' : ['2018.01.01','2019.02.02','2020.03.03'] }

for key, values in day.items():
    #print(values)
    for i in values:
        #print( i )
        v = i.split(".")
        #print( v )
        print( f"{v[0]}년 {v[1]}월 {v[2]}일")   #2018년 01월 01일\n2019년 02월 02일\n2020년 03월 03일

print('='*20)

day = { '날짜' : ['2018.01.01','2019.02.02','2020.03.03'] }

ls = list( map(lambda x : x.split("."), day['날짜']) )
for i in ls:
    print(f"{i[0]}년 {i[1]}월 {i[2]}일")    ##2018년 01월 01일\n2019년 02월 02일\n2020년 03월 03일
    
print('='*20)

# ex 2 ) def -------> lambda 
def test2( x ):
    print(x,"입니다")   #1000 입니다
test2(1000)
ls = [10,20,30]
ls = list(map(int, ls))

a = lambda x : print(x,"입니다")
a(1234) #1234 입니다











