"""�Լ�"""
# Q1 ����+���ϰ�
def sum1(a,b):
    return a+b

print(sum1(1,2))

# Q2 ����+����X
def sub(a,b):
    print(a-b)

sub(1,2)

# Q3 ����X+����X
def hungry():
    print("����Ŀ�")

hungry()

# �μ� ������ �ޱ�
"""�μ��� ������ ������ �ȹް� �ʹٸ� �μ� �տ� '*'�� �ٿ��־� Ʃ�÷� �����."""
def sum2(*a):
    total = 0
    for i in a :
        total += i
    return print(total)

sum2(1,2,3)
sum2(1,2,3,4)

# ����Ʈ ����
def cal(num1, num2, method='sum'): # default�� sum (deault�� ������ �μ��� �ݵ�� ������ �κп� ��ġ)
    if method == 'sum':
        print(num1+num2)
    elif method == 'sub':
        print(num1-num2)
    elif method == 'prod':
        print(num1*num2)

cal(1,2)
cal(1,2,'prod')
cal(1,2,'sub')

