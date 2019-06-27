""" Naver Open API를 이용하여 네이버 이미지를 다운받는 크롤러 만들기 """

import urllib.request # 웹을 열어서 데이터 가져오는 모듈
import urllib.parse # url에 한글 검색어를 입력할 수 있도록 도와주는 모듈
import re
from bs4 import BeautifulSoup

def input_query():
    q = urllib.parse.quote_plus(str(input("검색어를 입력하세요: "))) # 검색어 인코딩(공백을 +기호로 처리)
    return "&query="+ q

def bind_url():
    default_url = "https://openapi.naver.com/v1/search/image.xml?"
    query = input_query()
    sort = "&sort=sim" # 요청 변수는 &로 연결한다. // sim(default), date, count, point가 있다.
    start = '&start=1'
    display = "&display=100"
    full_url = default_url + sort + start + display + query
    return full_url

def fetch_contents_from_url():
    headers = {
    'Host' : 'openapi.naver.com',
    'User-Agent' : 'curl/7.49.1',
    'Accept' : '*/*',
    'Content-Type' : 'application/xml',
    'X-Naver-Client-Id' : 'GoxxVGwr0zSL9s0rIVTd',
    'X-Naver-Client-Secret' : 'Fv56o_I8qC',
    }
    url = bind_url()
    r = urllib.request.Request(url, headers=headers) # HTTP 요청 전, 헤더 정보를 이용해 request 객체 생성
    f = urllib.request.urlopen(r) # # 헤더 정보를 포함하여 서버에게 HTTP 요청.
    html = f.read() # 요청된 데이터를 xml로 읽어들임.
    return html

# HTML에서 꺼낸 태그들을 리스트로 넘겨주면 정규식을 사용해서 텍스트만 남겨주는 역할.
def extract_text_in_tags(tags, tagname='title'):
    txt=[]
    reg = "[^<" + tagname + ">][^<]+"
    for tag in tags :
        txt.append(re.search(reg,tag).group())
    return txt # 텍스트 리스트 반환.

def get_contents_from_html():
    html = fetch_contents_from_url()
    title_tags = re.findall("<title>[^<]+</title>", html.decode('utf-8')) # title 태그들을 찾아서 리스트로 저장
    link_tags = re.findall("<link>[^<]+</link>", html.decode('utf-8')) # link 태그들을 찾아서 리스트로 저장
    titles = extract_text_in_tags(title_tags, tagname = 'title') # title 태그의 텍스트를 가져옴.
    links = extract_text_in_tags(link_tags, tagname = 'link') # link 태그의 텍스트를 가져옴.
    f = open("image.html", "w")
    f.write("<html><body>")
    for i in range(1, len(titles)):
        f.write("<p>"+titles[i]+"</p>") # p태그에 타이틀 넣기
        f.write("<img src = " + links[i] + "/>") # 이미지 파일경로 넣어주기.
    f.write("</body></html>")
    f.close

get_contents_from_html()