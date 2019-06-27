"""함수"""
# Q1 인자+리턴값
def sum1(a,b):
    return a+b

print(sum1(1,2))

# Q2 인자+리턴X
def sub(a,b):
    print(a-b)

sub(1,2)

# Q3 인자X+리턴X
def hungry():
    print("배고파요")

hungry()

# 인수 여러개 받기
"""인수의 개수에 제한을 안받고 싶다면 인수 앞에 '*'를 붙여주어 튜플로 만든다."""
def sum2(*a):
    total = 0
    for i in a :
        total += i
    return print(total)

sum2(1,2,3)
sum2(1,2,3,4)

# 디폴트 인자
def cal(num1, num2, method='sum'): # default가 sum (deault를 설정한 인수는 반드시 마지막 부분에 위치)
    if method == 'sum':
        print(num1+num2)
    elif method == 'sub':
        print(num1-num2)
    elif method == 'prod':
        print(num1*num2)

cal(1,2)
cal(1,2,'prod')
cal(1,2,'sub')

