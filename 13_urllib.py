"""urllib 라이브러리"""
# urllib 라이브러리는 Python에서 웹과 관련된 데이터를 쉽게 이용하게 도와주는 라이브러리

# requst 모듈
import urllib.request # 웹을 열어서 데이터 가져오는 모듈
req = urllib.request
d = req.urlopen("http://www.naver.com") # 웹페이지 불러오기
status = d.getheaders()
for s in status:
    print(s)

# 웹 페이지의 상태 확인
print(d.status) # 200 은 정상출력 의미.

# 웹 페이지의 데이터 읽기
print(d.read()) # html 코드 출력.

# parse 모듈
import urllib.parse # url에 한글 검색어를 입력할 수 있도록 도와주는 모듈
def input_query():
    q = str(input("검색어를 입력하세요: ")) # 그냥 검색
    return "&query=" + q

print(input_query()) # &query=검색어

def input_query():
    q = urllib.parse.quote_plus(str(input("검색어를 입력하세요: "))) # 인코딩해서 검색(컴퓨터가 알아들을 수 있게)
    return "&query=" + q

print(input_query()) # &query=%EC%82%AC%EC%9A%A9%EC%95%88%ED%95%A8
print(urllib.parse.quote("검색어")) # 공백을 %20으로 인코딩
print(urllib.parse.quote_plus("검색어")) # 공백을 +로 인코딩