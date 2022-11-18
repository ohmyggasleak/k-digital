	
# [문항1] 1.아래의 내용을 보고 문제를 해결하시오(풀이 코드 올려주세요)

# 1).입력한 데이터가 3의 배수인 경우 출력 하시오.
num=int(input("수 입력: "))
if num%3==0:
    print("{} : 3의 배수.".format(num))
else:
    print("{} : 3의 배수가 아닙니다.".format(num))

# 2).수를 입력 받아 짝,홀수를 구분하여 출력 하시오.
su = int(input("수 입력: "))
if su % 2 ==0:
    print("{} : 짝수.".format(su))
else:
    print("{} : 홀수.".format(su))

# 3).두수를 입력 받아 큰 수를 출력 하시오.
n1 = int(input("수 입력: "))
n2 = int(input("수 입력: "))
if n1>n2 :
    print(f"큰수 : {n1}" )
elif n1<n2:
    print(f"큰수 : {n2}" )
else:
    print(f"{n1}={n2} 같습니다.")
# 4).수를 입력받아 절대값을 구하는 프로그램을 작성 하시오.
num_=int(input("수 입력: "))
abs_num=0
if num_<0:
    abs_num = -num_
    print(f"{num_}의 절대값은 {abs_num}입니다.")
else:
    print(f"{num_}의 절대값은 {num_}입니다.")



# [문항2] 2.아래의 내용을 보고 문제를 해결하시오(풀이 코드 올려주세요)

# 1).날짜를 입력 받아 요일을 구하시오.
# 단, 1일은 무조건 월요일이다. 7일은 일요일, 8일은 다시 월요일
# 어떤 값을 입력 받던 요일이 정확히 출력 되게 만드시오.
n=int(input("날짜 입력: "))
if n%7==1:
    print(f"{n}일은 월요일입니다.")
elif n%7==2:
    print(f"{n}일은 화요일입니다.")
elif n%7 ==3:
    print(f"{n}일은 수요일입니다.")
elif n%7 ==4:
    print(f"{n}일은 목요일입니다.")
elif n%7 ==5:
    print(f"{n}일은 금요일입니다.")
elif n%7 ==6:
    print(f"{n}일은 토요일입니다.")
elif n%7 ==0:
    print(f"{n}일은 일요일입니다.")


# 2).세수를 입력 받아 큰 수를 출력 하시오.
n1 = int(input("수 입력: "))
n2 = int(input("수 입력: "))
n3 = int(input("수 입력: "))
if n1>n2 and n1>n3 :
    print(f"큰 수 : {n1}")
elif n2>n1 and n2>n3 :
    print(f"큰 수 : {n2}")
elif n3>n1 and n3>n2 :
    print(f"큰 수 : {n3}")

# 3).두수를 입력 받아 큰 수가 짝수이면 출력 하시오.
n1 = int(input("수 입력: "))
n2 = int(input("수 입력: "))
if n1>n2:
    if n1%2==0:
        print(f"{n1} 큰 수 이면서 짝수")
elif n2>n1:
    if n2%2==0:
        print(f"{n2} 큰 수 이면서 짝수")


# 4).두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력 하시오.
n1 = int(input("수 입력: "))
n2 = int(input("수 입력: "))
sum_=n1+n2
if sum_%2==0:
    if sum_%3==0:
        print(f"{n1},{n2} 수의 합이 짝수이고 3의 배수")



# 문항3] 3.아래의 내용을 보고 문제를 해결하시오(풀이 코드 올려주세요)

# 1).1~100 까지의 총 합을 구한다. 단, 3의 배수는 제외하고 3의 배수이며 5의 배수는 제외하지 않는 조건이다.
# 3의 배수는 제외
# 3의 배수이며 5의배수는 제외하지않는다.
sum_=0
for i in range(1,101):
    if i%3 !=0:
        sum_ += i
        
    if i%3==0 and i%5==0:
        sum_ +=i

print(sum_)

        
        
# 2).두 수를 입력 받아 입력 받은 두 수의 범위 안의 합을 구하시오
# 1입력, 10입력 => 55
# 10입력,1입력 => 55

n1 = int(input("수 입력: "))
n2 = int(input("수 입력: "))
sum_=0
if n1>n2:
    n1, n2 = n2, n1
for i in range(n1,n2+1):
    sum_+=i
print(f"두 수의 합{sum_}")


# 3).첫날에 10원을 예금하고, 다음날에는 전날의 2배를 예금하는 방식으로 한달(30일) 이 되는 날 입금해야 하는 금액은 얼마인지 구하시오
# (첫날 10, 둘 째날 20 , 셋 째날 40 . . .무조건 2배씩 증가되는 값이다)

firstday = 10
count=0
while count<30:
    count+=1
    if count==1:
        firstday=10
    else:
        firstday *=2
print("{}째날, {:,}원".format(count,firstday))




# 4) 아래와 같이 출력되게 2중 for문을 이용하여 출력하시오
# 상위포문 0 일 때 하위 포문 : 0 0 0 0 0
# 상위포문 1 일 때 하위 포문 : 0 1 2 3 4
# 상위포문 2 일 때 하위 포문 : 0 2 4 6 8
# 상위포문 3 일 때 하위 포문 : 0 3 6 9 12
# 상위포문 4 일 때 하위 포문 : 0 4 8 12 16
	
for i in range(5):
    print(f"상위포문 {i}일 때 하위 포문 :",end=" ")
    for j in range(5):
        print(f"{i*j}",end=" ")
    print()



# [문항4] 4. 랜덤과 set을 이용하여 로또 프로그램을 만드시오
from random import randrange
lotto = set()
while len(lotto)<6:
    lotto.add(randrange(1,46))
print(lotto)




# 문항5] 5. 다음 내용을 lambda와 map을 이용하여 아래와 같이 표현하시오
# day = { '날짜' : ['2018.01.01','2019.02.02','2020.03.03'] }

# 2018년 01월 01일
# 2019년 02월 02일
# 2020년 03월 03일

day = { '날짜' : ['2018.01.01','2019.02.02','2020.03.03'] }
result = map(lambda x : x.split('.'),day['날짜'])
for i in result:
    print("{}년 {}월 {}일".format(i[0],i[1],i[2]))




