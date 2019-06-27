"""2단부터 4단까지 출력되는 구구단을 for문과 while문으로 각각 작성하세요."""
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

"""숫자를 입력받고 출력되는 구구단을 for문과 while문으로 각각 작성하세요."""
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
print옵션
sep='!' 문자들사이에 공백 대신 ! 삽입
end=' ' 마지막에 개행대신 공백
"""
print("안녕", "하세요")
print("안녕", "하세요", sep='!')
print("안녕", end='')
print("하세요")

"""for문을 사용하여 구구단 11단부터 16단까지를 각 단수가 한줄에 출력"""
for i in range(11,17):
    for j in range(1,10):
        print(i, "x", j, "=", i*j, end =' ')
        if j == 9:
            print("")

"""간단한 데이터 파싱"""
str_data = "{a1:b1}, {a2:b2}, {a3:b3}, {a4:b4}, {a5:b5}"
split_str_data = str_data.split(",")
for i in range(len(split_str_data)):
    data = split_str_data[i].split(":")[1].split("}")[0]
    print(data)

