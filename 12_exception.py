"""����ó���� ���ô�"""
# Ex) ����ڿ��� 1-4���� ���ڸ� �Է��϶�� �޽��� �����ְ� ����ڰ� 5�� �Է�.
# -> ���� ����

# Q1
try:
    num = int(input("���ڸ� �Է��� �ּ���"))
except ValueError:
    print("���ڰ� �ƴմϴ�.")

# Q2
try:
    no1 = 6
    no2 = 0
    no1 / no2
except ZeroDivisionError: # �ڵ����� � �������� �� �� �ִ�.
    print("0���� ���� �� �����ϴ�.")

# Q3
try:
    no1 = int(input("ù ��° ���ڸ� �Է��� �ּ���"))
    no2 = int(input("�� ��° ���ڸ� �Է��� �ּ���"))
    no1 / no2
except (ZeroDivisionError, ValueError): # ���� �� ����ó��
    print("0���� ���� �� �����ϴ�.")

# finally : ������ �߻����� ������� ������ ����
try:
    num = int(input("���ڸ� �Է��� �ּ���"))
except ValueError:
    print("���ڰ� �ƴմϴ�.")
else:
    print(num) # ������ �ƴϸ� ���
finally:
    print("finally�� ������ ����˴ϴ�.")

# raise : ���� �����
try:
    num = int(input('���ڸ� �Է��ϼ��� : '))
    raise ValueError("0���� �۾ƿ�", "0�̿���", "0���� Ŀ��")
except ValueError as e :
    if num < 0 :
        print(e.args[0])
    elif num == 0 :
        print(e.args[1])
    elif num > 0 :
        print(e.args[2])    