"""���ǹ��� �ݺ���"""
# ���̽��� ��� �鿩���Ⱑ �ſ� �߿��ϴ�.
# '�׸���' '�Ǵ�' �� ��� and �� or�� ǥ���Ѵ�.

# Q1. if��
score = int(input("������ �Է����ּ��� : "))
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

# Q2. if��
num = int(input("���ڸ� �Է��ϼ��� : "))
if num == 0 :
    print("����")
elif num == 1 or num != 2:
    print("���")
else:
    print("����")

# Q3. for��
list = ["��", "��", "����"]
for i in list:
    print(i)

str = "�ȳ��Ͻʴϱ�?"
for i in str:
    print(i)

# Q4. for��
for i in (1,2,3,4):
    print(i)

for i in range(1,5): # range 1���� 5������
    print(i)

# Q5. while��
a = 0
while a < 5:
    print(a)
    a += 1

# break���� continue��
a = ["���1", "���2", "���3", "����", "���4"]
for i in a:
    if i == "����":
        print("����")
        break
    else:
        print(i)

for i in range(0,10):
    if i%2 == 0:
        print(i)
    else:
        continue
