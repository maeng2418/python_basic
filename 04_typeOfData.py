"""����������"""
a = 3
print (a)
a += 3
print (a)

# a++�� ++a�� ����� �� ����.

# ������ ��ȯ(��)
no1 = input("first Num : ")
no2 = input("second Num : ")
print (no1 + no2)

# ������ ��ȯ(��)
no1 = int(input("first Num : "))
no2 = int(input("second Num : "))
print (no1 + no2)

# �Ǽ�
no3 = 10
print(float(no3))

# ���ڿ� �ε���
str = "Hello_Everyone"
print(str[0])
print(str[0:5]) # 0������ 5�������� ����
print(str[5])
print(str[4:]) # 4������ ��� ���
print(str[0:-2]) # 0������ �ڿ��� 2��° ������

# ��Ÿĳ����
str1 = "��\n�ٲ��"
str2 = "\t 8ĭ �鿩����"
str3 = "��\\n�ٲ�������"
print(str1)
print(str2)
print(str3)

# �ҹ��� �빮��
str = "APple"
print(str.upper())
print(str.lower())

# Ư�� ���� ���� ã��
str = "�Ʊ�ٸ� ���ٸ� �� �����̴�~!"
print(str.count("��")) # ��ü
print(str.count("��",0)) # 0������
print(str.count("��",2)) # 2������

# Ư�� ���ڰ� �ִ� ��ġ ã��
print(str.index("��"))
print(str.index("��", 2)) # 2������

# ��������
str1 = " ���� �� ��������"
str2 = "������ �� �������� "
str3 = " ���� �� �������� "
print(str1.lstrip())
print(str2.rstrip())
print(str3.strip())

# ���ڿ� �ٲٱ�
str = "������ ���� ������"
print(str.replace("������", "���"))
str = "a-a-a-a-a"
print(str.replace("a","b")) # �� �ٲ�
print(str.replace("a","b",3)) # 3���� �ٲ�

# ���ڿ� ������
str = "�ȳ��ϼ��� ���� ��� �Դϴ�."
print(str.split(" ")) # ���� �������� ������
print(str.split(" ", 2)) # ���� �������� 2���� ������

# ���ڿ� ����
str = "���� ����� ����."
print(len(str))

# ���ڿ� ����
print("*" * 20)

# ���� ���� ���ڿ� ����
str = '''ȫ�浿
������
������'''
print(str)

# ���ڸ� ���ڷ�
num1 = 2
num2 = 3
print(num1 + num2)
print(str(num1)+str(num2))