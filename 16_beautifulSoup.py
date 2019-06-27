"""BeautifulSoup 라이브러리"""

from bs4 import BeautifulSoup

"""
import urllib.request # 웹을 열어서 데이터 가져오는 모듈
req = urllib.request
html = req.urlopen("http://www.naver.com") # 웹페이지 불러오기
"""

html = """
<html>
    <head>
        <title> test web </title>  
    </head>
    <body>
        <p align = "center"> text content 1 </p>
        <p align = "right"> text content 2 </p>
        <p align = "left"> text content 3 </p>
        <img src = "C:\\Users\\김명성\\Desktop\\파이썬\\python.jpg" width="500"></img>
        <div class = "divtag black" align= "center"> text contents 1 </div>
        <div class = "divtag yellow" align= "center"> text contents 2 </div>
        <div class = "divtag red" align= "center"> text contents 3 </div>
    </body>
</html>
"""

bs = BeautifulSoup(html)
print("\n페이지 소스 조회")
print(bs.prettify())

############################################################################
""" find() 함수 - 태그를 하나만 가져 옵니다. """
############################################################################

# 태그 조회
print("\ntitle 태그 소스 조회")
print(bs.find('title')) 

############################################################################
""" find_all() 함수 - 해당 태그가 여러개 있을 경우 한꺼번에 모두 가져옵니다. """
############################################################################

# 여러개 한번에 조회
print("\np 태그 여러개 한번에 조회")
print(bs.find_all('p')) 

# head안의 title 조회
head = bs.find('head')
print("\nhead 태그 조회")
print(head)

print("\nhead안에 title 태그 조회")
print(head.find('title'))

# body안 p태그와 이미지 조회
print("\nbody안 p태그와 img태그 조회")
body = bs.find("body")
list = body.find_all(['p', 'img'])

for tag in list:
    print(tag)

# 정규식 사용해서 조회
import re
tag = bs.find_all(re.compile("^p"))
print("\n정규식 사용해서 조회")

print(tag) # p태그 조회

print(bs.find_all(text = re.compile(" text +"))) # text 인수는 문자열, 정규식, 리스트 등 여러가지를 인수로 전달 가능

print(bs.find_all("p", limit=2)) # 두개만 찾음.

############################################################################
""" 문장 가져오기. """
############################################################################

# Q1
body = bs.find('body')
p = body.find('p')
print("\n태그의 문장 하나를 가져옴.")
print(p.string) # 태그의 문장을 가져옴.

# Q2
print("\n태그의 모든 문장들을 가져옴.")
strings = body.strings # 태그 안에 있는 모든 문장들이 저장
for string in strings:
    print(string)

# Q3
body = bs.find('body')
print("\n모든 문자열을 하나의 문자열로 돌려줌.")
print(body.get_text()) # 모든 문자열을 하나의 문자열로 돌려줌.

# Q4
print("\n문장의 끝에 기호를 넣어 구분하여 모든 문자열을 하나의 문자열로 돌려줌.")
print(body.get_text('-', strip=True)) # 문장의 끝에 기호를 넣어 구분

############################################################################
""" 태그의 속성 가져오기. """
############################################################################

# class 속성 조회
print('\nclass 속성 조회.')
div_tag = bs.find('div')
print(div_tag['class'])

# class 속성 변경
print('\nclass 속성 변경.')
div_tag = bs.find('div')
div_tag['class'][1] = 'white'
print(div_tag['class'])

# class 속성 추가
print('\nclass 속성 추가.')
div_tag = bs.find('div')
div_tag['id'] = "D-TAG"
print(div_tag['id'])

# class 속성 삭제
print('\nclass 속성 삭제.')
div_tag = bs.find('div')
del div_tag['align']
print(bs.find('div'))

############################################################################
""" 태그의 관계. """
############################################################################

# 자식 리스트 출력
print('\n자식 리스트 출력')
body_tag = bs.find('body')
for child in body_tag.children:
    print(child)

# 부모 태그 출력
print('\n부모 태그 출력')
child_tag = bs.find('img')
print(child_tag.parent)

############################################################################
""" find_parent() 함수와 find_parents() 함수 """
############################################################################

# 자기의 부모 중 하나를 찾음.
p_tag = bs.find('p')
print('\n자기의 부모 중 하나를 찾음.')
print(p_tag.find_parent('body')) # find랑 별반 차이는 없음.

# 부모를 모두 찾음.
p_tag = bs.find('p')
print('\n자기의 부모 모두를 찾음.')
parents = p_tag.find_parents()
for parent in parents:
    print(parent.name)