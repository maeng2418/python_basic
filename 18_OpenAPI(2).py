""" Naver Open API�� �̿��Ͽ� ���̹� �̹����� �ٿ�޴� ũ�ѷ� ����� """

import urllib.request # ���� ��� ������ �������� ���
import urllib.parse # url�� �ѱ� �˻�� �Է��� �� �ֵ��� �����ִ� ���
import re
from bs4 import BeautifulSoup

def input_query():
    q = urllib.parse.quote_plus(str(input("�˻�� �Է��ϼ���: "))) # �˻��� ���ڵ�(������ +��ȣ�� ó��)
    return "&query="+ q

def bind_url():
    default_url = "https://openapi.naver.com/v1/search/image.xml?"
    query = input_query()
    sort = "&sort=sim" # ��û ������ &�� �����Ѵ�. // sim(default), date, count, point�� �ִ�.
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
    r = urllib.request.Request(url, headers=headers) # HTTP ��û ��, ��� ������ �̿��� request ��ü ����
    f = urllib.request.urlopen(r) # # ��� ������ �����Ͽ� �������� HTTP ��û.
    html = f.read() # ��û�� �����͸� xml�� �о����.
    return html

# HTML���� ���� �±׵��� ����Ʈ�� �Ѱ��ָ� ���Խ��� ����ؼ� �ؽ�Ʈ�� �����ִ� ����.
def extract_text_in_tags(tags, tagname='title'):
    txt=[]
    reg = "[^<" + tagname + ">][^<]+"
    for tag in tags :
        txt.append(re.search(reg,tag).group())
    return txt # �ؽ�Ʈ ����Ʈ ��ȯ.

def get_contents_from_html():
    html = fetch_contents_from_url()
    title_tags = re.findall("<title>[^<]+</title>", html.decode('utf-8')) # title �±׵��� ã�Ƽ� ����Ʈ�� ����
    link_tags = re.findall("<link>[^<]+</link>", html.decode('utf-8')) # link �±׵��� ã�Ƽ� ����Ʈ�� ����
    titles = extract_text_in_tags(title_tags, tagname = 'title') # title �±��� �ؽ�Ʈ�� ������.
    links = extract_text_in_tags(link_tags, tagname = 'link') # link �±��� �ؽ�Ʈ�� ������.
    f = open("image.html", "w")
    f.write("<html><body>")
    for i in range(1, len(titles)):
        f.write("<p>"+titles[i]+"</p>") # p�±׿� Ÿ��Ʋ �ֱ�
        f.write("<img src = " + links[i] + "/>") # �̹��� ���ϰ�� �־��ֱ�.
    f.write("</body></html>")
    f.close

get_contents_from_html()