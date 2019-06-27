"""조건문과 반복문"""
# 파이썬의 경우 들여쓰기가 매우 중요하다.
# '그리고' '또는' 의 경우 and 와 or로 표기한다.

# Q1. if문
score = int(input("점수를 입력해주세요 : "))
if score >= 90 and score <= 100:
    print('A+')
elif score >=80 and score <90:
    print('A')
elif score >=50 and score <80:
    print('B+')
elif score >30:
    print('B')
else:
    print('C')

# Q2. if문
num = int(input("숫자를 입력하세요 : "))
if num == 0 :
    print("종료")
elif num == 1 or num != 2:
    print("계속")
else:
    print("중지")

# Q3. for문
list = ["원", "투", "쓰리"]
for i in list:
    print(i)

str = "안녕하십니까?"
for i in str:
    print(i)

# Q4. for문
for i in (1,2,3,4):
    print(i)

for i in range(1,5): # range 1부터 5전까지
    print(i)

# Q5. while문
a = 0
while a < 5:
    print(a)
    a += 1

# break문과 continue문
a = ["계속1", "계속2", "계속3", "멈춤", "계속4"]
for i in a:
    if i == "멈춤":
        print("종료")
        break
    else:
        print(i)

for i in range(0,10):
    if i%2 == 0:
        print(i)
    else:
        continue
