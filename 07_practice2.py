"""2�ܺ��� 4�ܱ��� ��µǴ� �������� for���� while������ ���� �ۼ��ϼ���."""
# for
for i in range(2,5):
    for j in range(1,10):
        print(i, "x", j, "=", i*j)
        if j == 9:
            print("")

# while
i = 2
while i <= 4:
    j = 1
    while j < 10:
        print(i, "x", j, "=", i*j)
        if j == 9:
            print("")
        j+=1 
    i+=1

"""���ڸ� �Է¹ް� ��µǴ� �������� for���� while������ ���� �ۼ��ϼ���."""
# for
num = int(input("Enter the num : "))
for i in range(0,10):
    print(num, "x", i, "=", num*i)

# while
num = int(input("Enter the num : "))
i = 1
while i < 10:
    print(num, "x", i, "=", num*i)
    i+=1

"""
print�ɼ�
sep='!' ���ڵ���̿� ���� ��� ! ����
end=' ' �������� ������ ����
"""
print("�ȳ�", "�ϼ���")
print("�ȳ�", "�ϼ���", sep='!')
print("�ȳ�", end='')
print("�ϼ���")

"""for���� ����Ͽ� ������ 11�ܺ��� 16�ܱ����� �� �ܼ��� ���ٿ� ���"""
for i in range(11,17):
    for j in range(1,10):
        print(i, "x", j, "=", i*j, end =' ')
        if j == 9:
            print("")

"""������ ������ �Ľ�"""
str_data = "{a1:b1}, {a2:b2}, {a3:b3}, {a4:b4}, {a5:b5}"
split_str_data = str_data.split(",")
for i in range(len(split_str_data)):
    data = split_str_data[i].split(":")[1].split("}")[0]
    print(data)

