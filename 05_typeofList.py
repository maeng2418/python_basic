"""����Ʈ ����"""
list = [1, "�ȳ��Ͻʴϱ�", 10] # �ٸ� ���ó�� �迭�� �ϳ��� ������ �������� ���ǵ� �ʿ䰡 ����.

print("%d" %list[0])
print("%s" %list[1])
print("%f" %list[2])

# ������ �߰��ϱ�
list.append("�߰�")
print(list[3])

# �߰��� �����ϱ�
print(list)
list.insert(1,"����")
print(list)

# ������ �����ϱ�
del list[0] # �ε����� ����
print(list)
list.remove("�߰�") # �ش� ������ ����
print(list)

# ������ �����ϱ�
num = [1,3,2,5,4,6]
num.sort()
print(num)
num.reverse()
print(num)

alpha = ["a", "C", "b", "f", "D"] # �빮�� ���� ����
alpha.sort()
print(alpha)

# ������ ��ġ ã��
foods = ["«��", "������", "��ǳ��", "¥���"]
print(foods.index('��ǳ��'))

# ����Ʈ �ȿ� ����Ʈ
foods = ["«��", "���", ["�Ľ�Ÿ", "���"]]
print(foods[2])
print(foods[2][1])
print(foods[2][0:1])

# ����Ʈ ����
list = [1,2,3,4,5,[2,3,4,5,6]]
print(len(list))

# Ʃ��
"""Ʃ���� ������ �Ŀ��� ������ �����ϴ� ���� �Ұ����ϴ� & �Ұ�ȣ�� ����Ѵ�."""
tup = (1, "�ȳ��Ͻ÷ƴϱ�?", 10)
print (tup[0])

# ��ųʸ�
dictionary = {
    '��ġ' : "tuna",
    '���' : 'kimbap',
    '����' : 'fruit'
}

print(dictionary['���'])

# �����ϱ�
dictionary['���'] = "No data"
print(dictionary['���'])

# �����ϱ�
del dictionary['���']
# dictionary.remove('fruit') remove�� ���� �ȵ�. 
print(dictionary)

# Ű �� ��ȸ
print(dictionary.keys())
print(set(dictionary)) # ���� Ű���� ������

# �� ��ȸ
print(dictionary.values())

# �ʱ�ȭ
dictionary.clear()
print(dictionary)

# �ش�Ű�� �ִ��� ������ ��ȸ
dictionary = {
    '��ġ' : "tuna",
    '���' : 'kimbap',
    '����' : 'fruit'
}
print('��' in dictionary)
print('��ġ' in dictionary)