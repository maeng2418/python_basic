"""Ŭ����"""
# Ŭ������ ��İ� ���� �����̴� �⺻ ������ �������� �ʿ��Ҷ����� ������ ���븸 �ٲپ ����Ѵ�.
# ������ �Լ��� ��Ƴ��� ����
class bread:
    meterial = "��"

first_bread = bread()
print(first_bread.meterial)

second_bread = bread()
second_bread.meterial = '��ũ��'
print(second_bread.meterial)

# Ŭ���� �ȿ� �Լ�
class ramen:
    flavor = "�ſ��"
    def say(self): # self�� �ν��Ͻ� �ڱ� �ڽ��� ����Ų��.(Ŭ�����ȿ� �Լ� ������ �� �ʿ�.)
        print("���� %s�Դϴ�." %self.flavor)

first_ramen = ramen()
first_ramen.say()

# ������ (�ν��Ͻ� ������ ���ÿ� ����)
class americano:
    def __init__(self, m):
        self.meterial = m
    def say(self):
        print("���� %s �Ƹ޸�ī��" %self.meterial)

first_americano = americano("Hot")
first_americano.say()

# ���
class human:
    def __init__(self, name):
        self.name = name
    def intro(self):
        print("�� �̸��� %s �Դϴ�." %self.name)

class child(human): # childŬ������ humanŬ���� ���
    def hello(self):
        print("���� %s 2�� �Դϴ�." %self.name)

adult = human("Kim")
adult.intro()
baby = child("Lee")
baby.intro()
baby.hello()