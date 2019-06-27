""" Naver Open API�� �̿��Ͽ� ���̹� ������ �˻��ϴ� ũ�ѷ� ����� """

import urllib.request # ���� ��� ������ �������� ���
import urllib.parse # url�� �ѱ� �˻�� �Է��� �� �ֵ��� �����ִ� ���
from bs4 import BeautifulSoup

defaultURL = "https://openapi.naver.com/v1/search/news.xml?"
sort = "&sort=sim" # ��û ������ &�� �����Ѵ�. // sim(default, ���絵��), date, count, point�� �ִ�.
start = '&start=1'
display = "&display=100"
query = "&query="+urllib.parse.quote_plus(str(input("�˻�� �Է��ϼ���: "))) # UTF-8 ���ڵ��ؼ� �˻�(��ǻ�Ͱ� �˾Ƶ��� �� �ְ�)(������ +��ȣ�� ó��)

fullURL = defaultURL + sort + start + display + query

print(fullURL) # ��û URL�� ����� ���յǾ����� Ȯ��.

file = open("C:\\Users\\���\\Desktop\\���̽�\\naver_news.txt", "w", encoding="euc-kr")

# HTTP ��û ��, ������ ���ø����̼� ������ ���� ������ �Ѱ��ֱ� ���� ����.
headers = {
    'Host' : 'openapi.naver.com',
    'User-Agent' : 'curl/7.49.1',
    'Accept' : '*/*',
    'Content-Type' : 'application/xml',
    'X-Naver-Client-Id' : 'GoxxVGwr0zSL9s0rIVTd',
    'X-Naver-Client-Secret' : 'Fv56o_I8qC',
}

req = urllib.request.Request(fullURL, headers=headers) # HTTP ��û ��, ��� ������ �̿��� request ��ü ����
f = urllib.request.urlopen(req) # ��� ������ �����Ͽ� �������� HTTP ��û.

resultXML = f.read() # ��û�� �����͸� xml�� �о����.
xmlsoup = BeautifulSoup(resultXML, "html.parser") # xml�� ��ƼǮ���� ��ü�� ����.

items = xmlsoup.find_all("item") # ��ƼǮ���� ��ü�� item�±׸� ��� ������.

for item in items :
    file.write('--------------------------------------------------\n')
    file.write('�������� : ' + item.title.get_text(strip=True) + '\n')
    file.write('��೻�� : ' + item.description.get_text(strip=True) + '\n')
    file.write('\n') 

file.close()   