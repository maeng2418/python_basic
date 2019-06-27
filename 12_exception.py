"""예외처리를 배웁시다"""
# Ex) 사용자에게 1-4까지 숫자를 입력하라고 메시지 보여주고 사용자가 5를 입력.
# -> 논리적 에러

# Q1
try:
    num = int(input("숫자를 입력해 주세요"))
except ValueError:
    print("숫자가 아닙니다.")

# Q2
try:
    no1 = 6
    no2 = 0
    no1 / no2
except ZeroDivisionError: # 코드실행시 어떤 에러인지 알 수 있다.
    print("0으로 나눌 수 없습니다.")

# Q3
try:
    no1 = int(input("첫 번째 숫자를 입력해 주세요"))
    no2 = int(input("두 번째 숫자를 입력해 주세요"))
    no1 / no2
except (ZeroDivisionError, ValueError): # 여러 개 예외처리
    print("0으로 나눌 수 없습니다.")

# finally : 에러의 발생여부 상관없이 무조건 실행
try:
    num = int(input("숫자를 입력해 주세요"))
except ValueError:
    print("숫자가 아닙니다.")
else:
    print(num) # 에러가 아니면 출력
finally:
    print("finally는 무조건 실행됩니다.")

# raise : 에러 만들기
try:
    num = int(input('숫자를 입력하세요 : '))
    raise ValueError("0보다 작아요", "0이예요", "0보다 커요")
except ValueError as e :
    if num < 0 :
        print(e.args[0])
    elif num == 0 :
        print(e.args[1])
    elif num > 0 :
        print(e.args[2])    