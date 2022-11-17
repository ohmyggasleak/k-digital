#sumFunc()처럼 입력도받고 for문쓰고 출력도 하는 함수를 강한결합 이라고 부름(나눠서 쓰는게 좋음)
# def sumFunc():
#     sum_ = 0 
#     num = int(input("수 입력: "))
#     for i in range(num+1):
#         sum_+=i
#     print(f"1~{num}까지의 합 : {sum_}")
# sumFunc()


# def sumFunc1(num):
#     sum_ = 0 
#     # num = int(input("수 입력: "))
#     for i in range(num+1):
#         sum_+=i
#     print(f"1~{num}까지의 합 : {sum_}")

# num = int(input("수 입력: "))
# sumFunc1(num)


# def sumFunc2(num):
#     sum_ = 0 
#     for i in range(num+1):
#         sum_+=i
#     return sum_

# num = int(input("수 입력: "))
# sum_=sumFunc2(num)
# print(f"1~{num}까지의 합 : {sum_}")


# # 연산, 출력, 입력 함수를 각각 만들어 동작
# def myInput():
#     num = int(input("수:"))
#     return num

# def myPrint(num,sum_):
#     print(f"1~{num}까지의 합 : {sum_}")

# def sumFunc3(num):
#     sum_ = 0 
#     for i in range(num+1):
#         sum_+=i
#     return sum_

# num = myInput()
# sum_=sumFunc3(num)
# myPrint(num,sum_)



# def myPrint(result):
#     print(result)

# def myInput():
#     num = int(input("수 입력:"))
#     return num

# def threeFunc(num):
#     if num%3==0:
#         result=f"{num}는 3의 배수입니다"
#     else:
#         result=f"{num}는 3의 배수가 아닙니다"

#     return result
# x=threeFunc(4)
# print(x)

# def sosuFunc(num):
#     cnt=0
#     for i in range(1,10):
#         if num%i==0:
#             cnt+=1
#     if cnt==2:
#         return f"{num}은 소수입니다"
#     return f"{num}은 소수가 아닙니다"
# n=myInput()
# r=sosuFunc(n)
# myPrint(r)


# def reverseFunction(num):
#     li = []
#     for i in range(len(str(num))):
#         x=num%10
#         li.append(x)
#         num=num//10
#     return li

# x=reverseFunction(456)
# print(x)

# def operation(num1,num2,k):
#     if k == '+':
#         print("두수의 합은 {}".format(num1+num2))
#     elif k == '-':
#         print("두수의 차는 {}".format(num1-num2))
#     elif k == '/':
#         print("두수의 나누기는 {}".format(num1/num2))
#     elif k == '*':
#         print("두수의 곱은 {}".format(num1*num2))









