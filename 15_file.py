"""���� ���� �� �����ϱ�"""

# ������
f = open("test.txt", "w")
f.write("�ؽ�Ʈ���� ����� �����Դϴ�.")
f.close()

# �̾��
f = open("test.txt", "a")
f.write("������ �߰��մϴ�.")
f.close()

# �ڵ����� ���� �ݱ� -> close�����ص� ��.
with open("test.txt", 'a') as f:
    f.write("\nwith �� �׽�Ʈ�Դϴ�.")

# �б���
with open("test.txt", "r") as f:
    lines = f.readlines()  # readline ���پ� ��� / readlines ����Ʈ�������� ���� �� ���
    for line in lines:
        print(line)

# ���� ������
with open("test.txt", "r") as f:
    print(f.readline())
    print(f.tell()) # �ѱ��� 2byte, \n�� 2����Ʈ

    f.seek(2) # ���� ������ �̵�
    print(f.readline())

# ���̳ʸ� ����
img = open("python.jpg", "rb")
img2 = open("python2.jpg", "wb")
img2.write(img.read()) # ����
img.close()
img2.close()

