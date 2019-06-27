""" Naver Open API를 이용하여 네이버 뉴스를 검색하는 크롤러 만들기 """

import urllib.request # 웹을 열어서 데이터 가져오는 모듈
import urllib.parse # url에 한글 검색어를 입력할 수 있도록 도와주는 모듈
from bs4 import BeautifulSoup

defaultURL = "https://openapi.naver.com/v1/search/news.xml?"
sort = "&sort=sim" # 요청 변수는 &로 연결한다. // sim(default, 유사도순), date, count, point가 있다.
start = '&start=1'
display = "&display=100"
query = "&query="+urllib.parse.quote_plus(str(input("검색어를 입력하세요: "))) # UTF-8 인코딩해서 검색(컴퓨터가 알아들을 수 있게)(공백을 +기호로 처리)

fullURL = defaultURL + sort + start + display + query

print(fullURL) # 요청 URL이 제대로 조합되었는지 확인.

file = open("C:\\Users\\김명성\\Desktop\\파이썬\\naver_news.txt", "w", encoding="euc-kr")

# HTTP 요청 시, 서버에 애플리케이션 정보에 대한 정보를 넘겨주기 위한 변수.
headers = {
    'Host' : 'openapi.naver.com',
    'User-Agent' : 'curl/7.49.1',
    'Accept' : '*/*',
    'Content-Type' : 'application/xml',
    'X-Naver-Client-Id' : 'GoxxVGwr0zSL9s0rIVTd',
    'X-Naver-Client-Secret' : 'Fv56o_I8qC',
}

req = urllib.request.Request(fullURL, headers=headers) # HTTP 요청 전, 헤더 정보를 이용해 request 객체 생성
f = urllib.request.urlopen(req) # 헤더 정보를 포함하여 서버에게 HTTP 요청.

resultXML = f.read() # 요청된 데이터를 xml로 읽어들임.
xmlsoup = BeautifulSoup(resultXML, "html.parser") # xml을 뷰티풀수프 객체로 만듦.

items = xmlsoup.find_all("item") # 뷰티풀수프 객체에 item태그를 모두 가져옴.

for item in items :
    file.write('--------------------------------------------------\n')
    file.write('뉴스제목 : ' + item.title.get_text(strip=True) + '\n')
    file.write('요약내용 : ' + item.description.get_text(strip=True) + '\n')
    file.write('\n') 

file.close()   