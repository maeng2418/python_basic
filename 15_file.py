"""파일 생성 및 수정하기"""

# 쓰기모드
f = open("test.txt", "w")
f.write("텍스트파일 만들기 연습입니다.")
f.close()

# 이어쓰기
f = open("test.txt", "a")
f.write("내용을 추가합니다.")
f.close()

# 자동으로 열고 닫기 -> close사용안해도 됨.
with open("test.txt", 'a') as f:
    f.write("\nwith 절 테스트입니다.")

# 읽기모드
with open("test.txt", "r") as f:
    lines = f.readlines()  # readline 한줄씩 출력 / readlines 리스트형식으로 여러 줄 출력
    for line in lines:
        print(line)

# 파일 포인터
with open("test.txt", "r") as f:
    print(f.readline())
    print(f.tell()) # 한글은 2byte, \n도 2바이트

    f.seek(2) # 파일 포인터 이동
    print(f.readline())

# 바이너리 파일
img = open("python.jpg", "rb")
img2 = open("python2.jpg", "wb")
img2.write(img.read()) # 복사
img.close()
img2.close()

