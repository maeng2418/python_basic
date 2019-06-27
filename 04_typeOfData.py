"""데이터유형"""
a = 3
print (a)
a += 3
print (a)

# a++나 ++a는 사용할 수 없다.

# 정수형 변환(전)
no1 = input("first Num : ")
no2 = input("second Num : ")
print (no1 + no2)

# 정수형 변환(후)
no1 = int(input("first Num : "))
no2 = int(input("second Num : "))
print (no1 + no2)

# 실수
no3 = 10
print(float(no3))

# 문자열 인덱싱
str = "Hello_Everyone"
print(str[0])
print(str[0:5]) # 0번부터 5번전까지 문자
print(str[5])
print(str[4:]) # 4번부터 모두 출력
print(str[0:-2]) # 0번부터 뒤에서 2번째 전까지

# 메타캐릭터
str1 = "줄\n바꿔요"
str2 = "\t 8칸 들여쓰기"
str3 = "줄\\n바꾸지말기"
print(str1)
print(str2)
print(str3)

# 소문자 대문자
str = "APple"
print(str.upper())
print(str.lower())

# 특정 글자 개수 찾기
str = "아기다리 고기다리 던 방학이닷~!"
print(str.count("기")) # 전체
print(str.count("기",0)) # 0번부터
print(str.count("기",2)) # 2번부터

# 특정 문자가 있는 위치 찾기
print(str.index("기"))
print(str.index("기", 2)) # 2번부터

# 공백제거
str1 = " 왼쪽 끝 공백제거"
str2 = "오른쪽 끝 공백제거 "
str3 = " 양쪽 끝 공백제거 "
print(str1.lstrip())
print(str2.rstrip())
print(str3.strip())

# 문자열 바꾸기
str = "진수쌤 완전 동안임"
print(str.replace("진수쌤", "김명성"))
str = "a-a-a-a-a"
print(str.replace("a","b")) # 다 바꿈
print(str.replace("a","b",3)) # 3개만 바꿈

# 문자열 나누기
str = "안녕하세요 저는 김명성 입니다."
print(str.split(" ")) # 띄어쓰기 기준으로 나누기
print(str.split(" ", 2)) # 띄어쓰기 기준으로 2번만 나누기

# 문자열 길이
str = "나는 사과가 좋다."
print(len(str))

# 문자열 연산
print("*" * 20)

# 여러 줄의 문자열 저장
str = '''홍길동
유관순
일지매'''
print(str)

# 숫자를 문자로
num1 = 2
num2 = 3
print(num1 + num2)
print(str(num1)+str(num2))