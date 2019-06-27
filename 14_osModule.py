"""os���"""
# ������ �����Ѵٰų� ������ ���� ����ٰų� ������ ����� �� ���� �۾�.

import os

# ���� python�� �۾� ���� ���丮 ���
print(os.getcwd()) 

# ���� �۾� ���丮�� �����ϴ� �Լ�
os.chdir("C:\\temp")

# ���ϰ� ���� ����� ����Ʈ�� ��ȯ
print(os.listdir('C:\\Users\\���\\Desktop\\���̽�')) 
# for������ ���ϸ���Ʈ ���    
for name in os.listdir('C:\\Users\\���\\Desktop\\���̽�'):
    print(name)

# '�׽�Ʈ' ���� ����
os.mkdir('C:\\Users\\���\\Desktop\\���̽�\\�׽�Ʈ') 
# '�׽�Ʈ' ���� �� �������� ����
os.makedirs('C:\\Users\\���\\Desktop\\���̽�\\�׽�Ʈ0\\�׽�Ʈ1\\�׽�Ʈ2')

# text.txt ���ϻ���
os.remove("C:\\Python34\\text.txt") 
os.unlink("C:\\Python34\\text.txt")

# '�׽�Ʈ' ���� ����
os.rmdir('C:\\Users\\���\\Desktop\\���̽�\\�׽�Ʈ') 
# '�׽�Ʈ' ���� �� �������� ����
os.removedirs('C:\\Users\\���\\Desktop\\���̽�\\�׽�Ʈ0\\�׽�Ʈ1\\�׽�Ʈ2')

# ���� ���� �Ǵ��ϱ�
print(os.path.isdir("C:\\Users\\���\\Desktop\\���̽�")) # ���� ���� True
print(os.path.isdir("C:\\Users\\���\\Desktop\\���̽�.txt")) # ������ �ƴ� False
print(os.path.isdir("C:\\Users\\���\\Desktop\\���̽�X")) # ���� ����X False

# ���� ���� �Ǵ��ϱ�
print(os.path.isfile("C:\\Users\\���\\Desktop\\���̽�\\14_osModule.py")) # ���� ���� True
print(os.path.isfile("C:\\Users\\���\\Desktop\\osModule")) # ������ �ƴ� False
print(os.path.isfile("C:\\Users\\���\\Desktop\\osModule(X).py")) # ���� ����X False

# ������ ���� ���� �Ǵ��ϱ�
print(os.path.exists("C:\\Users\\���\\Desktop\\���̽�\\14_osModule.py")) # ������ ���� ���� True
print(os.path.exists("C:\\Users\\���\\Desktop\\osModule")) # ������ ������ �ƴ� False
print(os.path.exists("C:\\Users\\���\\Desktop\\osModule(X).py")) # ������ ���� ����X False

# ������ ũ�⸦ ��ȯ�� �ִ� �Լ�
print(os.path.getsize("C:\\Users\\���\\Desktop\\���̽�\\14_osModule.py"))

# ���ϰ� ������ ��θ� ������ �ִ� �Լ� (Ʃ�÷� ��ȯ)
print(os.path.split("C:\\Users\\���\\Desktop\\���̽�\\14_osModule.py"))
print(os.path.splitext("C:\\Users\\���\\Desktop\\���̽�\\14_osModule.py")) # Ȯ���ڶ� ����

# ���丮 ��θ� ��ȯ
print(os.path.dirname("C:\\Users\\���\\Desktop\\���̽�\\14_osModule.py"))
# �����̸��� ��ȯ
print(os.path.basename("C:\\Users\\���\\Desktop\\���̽�\\14_osModule.py"))

# ���� �̸��� ���� �̸��� �����ִ� �Լ�
splitPath = os.path.split("C:\\Users\\���\\Desktop\\���̽�\\14_osModule.py")
print(os.path.join(splitPath[0], splitPath[1]))
