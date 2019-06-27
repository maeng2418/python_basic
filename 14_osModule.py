"""os모듈"""
# 파일을 복사한다거나 폴더를 새로 만든다거나 파일을 지우는 것 같은 작업.

import os

# 현재 python이 작업 중인 디렉토리 출력
print(os.getcwd()) 

# 현재 작업 디렉토리를 변경하는 함수
os.chdir("C:\\temp")

# 파일과 폴더 목록을 리스트로 반환
print(os.listdir('C:\\Users\\김명성\\Desktop\\파이썬')) 
# for문으로 파일리스트 출력    
for name in os.listdir('C:\\Users\\김명성\\Desktop\\파이썬'):
    print(name)

# '테스트' 폴더 생성
os.mkdir('C:\\Users\\김명성\\Desktop\\파이썬\\테스트') 
# '테스트' 폴더 및 하위폴더 생성
os.makedirs('C:\\Users\\김명성\\Desktop\\파이썬\\테스트0\\테스트1\\테스트2')

# text.txt 파일삭제
os.remove("C:\\Python34\\text.txt") 
os.unlink("C:\\Python34\\text.txt")

# '테스트' 폴더 삭제
os.rmdir('C:\\Users\\김명성\\Desktop\\파이썬\\테스트') 
# '테스트' 폴더 및 하위폴더 삭제
os.removedirs('C:\\Users\\김명성\\Desktop\\파이썬\\테스트0\\테스트1\\테스트2')

# 폴더 유무 판단하기
print(os.path.isdir("C:\\Users\\김명성\\Desktop\\파이썬")) # 폴더 존재 True
print(os.path.isdir("C:\\Users\\김명성\\Desktop\\파이썬.txt")) # 폴더가 아님 False
print(os.path.isdir("C:\\Users\\김명성\\Desktop\\파이썬X")) # 폴더 존재X False

# 파일 유무 판단하기
print(os.path.isfile("C:\\Users\\김명성\\Desktop\\파이썬\\14_osModule.py")) # 파일 존재 True
print(os.path.isfile("C:\\Users\\김명성\\Desktop\\osModule")) # 파일이 아님 False
print(os.path.isfile("C:\\Users\\김명성\\Desktop\\osModule(X).py")) # 파일 존재X False

# 폴더나 파일 유무 판단하기
print(os.path.exists("C:\\Users\\김명성\\Desktop\\파이썬\\14_osModule.py")) # 폴더나 파일 존재 True
print(os.path.exists("C:\\Users\\김명성\\Desktop\\osModule")) # 폴더나 파일이 아님 False
print(os.path.exists("C:\\Users\\김명성\\Desktop\\osModule(X).py")) # 폴더나 파일 존재X False

# 파일의 크기를 반환해 주는 함수
print(os.path.getsize("C:\\Users\\김명성\\Desktop\\파이썬\\14_osModule.py"))

# 파일과 폴더의 경로를 구분해 주는 함수 (튜플로 반환)
print(os.path.split("C:\\Users\\김명성\\Desktop\\파이썬\\14_osModule.py"))
print(os.path.splitext("C:\\Users\\김명성\\Desktop\\파이썬\\14_osModule.py")) # 확장자랑 구분

# 디렉토리 경로만 반환
print(os.path.dirname("C:\\Users\\김명성\\Desktop\\파이썬\\14_osModule.py"))
# 파일이름만 반환
print(os.path.basename("C:\\Users\\김명성\\Desktop\\파이썬\\14_osModule.py"))

# 파일 이름과 폴더 이름을 합쳐주는 함수
splitPath = os.path.split("C:\\Users\\김명성\\Desktop\\파이썬\\14_osModule.py")
print(os.path.join(splitPath[0], splitPath[1]))
