'''
함수(메소드)
- class 안에 함수가 있으면 메소드라 호칭
- class 없이 함수만 있으면 함수
- 어떤 기능이 있다면 함수라고 한다.
- 소괄호가 존재하면 95%정도는 함수다.
사용방법
def test( args(argument 매개변수) ):
    종속문장
    return value

'''
def reverseCode():
    temp = 0
    result = int(input("수 입력: "))
    while True:
        temp = result %10
        result = result //10
        print(temp, end =", ")
        if result == 0 :
            break
    print("프로그램 종료")
print("시작")

if __name__ == "__main__":  # 현재 파일이 메인일 때 이 파일 내에선 reverseCode 함수 실행, 다른파일에서 불러오면 실행 안됨.
    print(1111)
    reverseCode()

print("종료")








