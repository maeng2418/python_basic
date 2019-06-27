""""모듈"""
# 클래스나 변수 또는 함수를 모아서 파일로 저장
import sys
sys.path.append("./modules")

# 모듈1
import practiceModule1
practiceModule1.hello()

# 모듈2
from practiceModule2 import hello, sleep
hello()
sleep()

