"""BeautifulSoup ���̺귯��"""

from bs4 import BeautifulSoup

"""
import urllib.request # ���� ��� ������ �������� ���
req = urllib.request
html = req.urlopen("http://www.naver.com") # �������� �ҷ�����
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
        <img src = "C:\\Users\\���\\Desktop\\���̽�\\python.jpg" width="500"></img>
        <div class = "divtag black" align= "center"> text contents 1 </div>
        <div class = "divtag yellow" align= "center"> text contents 2 </div>
        <div class = "divtag red" align= "center"> text contents 3 </div>
    </body>
</html>
"""

bs = BeautifulSoup(html)
print("\n������ �ҽ� ��ȸ")
print(bs.prettify())

############################################################################
""" find() �Լ� - �±׸� �ϳ��� ���� �ɴϴ�. """
############################################################################

# �±� ��ȸ
print("\ntitle �±� �ҽ� ��ȸ")
print(bs.find('title')) 

############################################################################
""" find_all() �Լ� - �ش� �±װ� ������ ���� ��� �Ѳ����� ��� �����ɴϴ�. """
############################################################################

# ������ �ѹ��� ��ȸ
print("\np �±� ������ �ѹ��� ��ȸ")
print(bs.find_all('p')) 

# head���� title ��ȸ
head = bs.find('head')
print("\nhead �±� ��ȸ")
print(head)

print("\nhead�ȿ� title �±� ��ȸ")
print(head.find('title'))

# body�� p�±׿� �̹��� ��ȸ
print("\nbody�� p�±׿� img�±� ��ȸ")
body = bs.find("body")
list = body.find_all(['p', 'img'])

for tag in list:
    print(tag)

# ���Խ� ����ؼ� ��ȸ
import re
tag = bs.find_all(re.compile("^p"))
print("\n���Խ� ����ؼ� ��ȸ")

print(tag) # p�±� ��ȸ

print(bs.find_all(text = re.compile(" text +"))) # text �μ��� ���ڿ�, ���Խ�, ����Ʈ �� ���������� �μ��� ���� ����

print(bs.find_all("p", limit=2)) # �ΰ��� ã��.

############################################################################
""" ���� ��������. """
############################################################################

# Q1
body = bs.find('body')
p = body.find('p')
print("\n�±��� ���� �ϳ��� ������.")
print(p.string) # �±��� ������ ������.

# Q2
print("\n�±��� ��� ������� ������.")
strings = body.strings # �±� �ȿ� �ִ� ��� ������� ����
for string in strings:
    print(string)

# Q3
body = bs.find('body')
print("\n��� ���ڿ��� �ϳ��� ���ڿ��� ������.")
print(body.get_text()) # ��� ���ڿ��� �ϳ��� ���ڿ��� ������.

# Q4
print("\n������ ���� ��ȣ�� �־� �����Ͽ� ��� ���ڿ��� �ϳ��� ���ڿ��� ������.")
print(body.get_text('-', strip=True)) # ������ ���� ��ȣ�� �־� ����

############################################################################
""" �±��� �Ӽ� ��������. """
############################################################################

# class �Ӽ� ��ȸ
print('\nclass �Ӽ� ��ȸ.')
div_tag = bs.find('div')
print(div_tag['class'])

# class �Ӽ� ����
print('\nclass �Ӽ� ����.')
div_tag = bs.find('div')
div_tag['class'][1] = 'white'
print(div_tag['class'])

# class �Ӽ� �߰�
print('\nclass �Ӽ� �߰�.')
div_tag = bs.find('div')
div_tag['id'] = "D-TAG"
print(div_tag['id'])

# class �Ӽ� ����
print('\nclass �Ӽ� ����.')
div_tag = bs.find('div')
del div_tag['align']
print(bs.find('div'))

############################################################################
""" �±��� ����. """
############################################################################

# �ڽ� ����Ʈ ���
print('\n�ڽ� ����Ʈ ���')
body_tag = bs.find('body')
for child in body_tag.children:
    print(child)

# �θ� �±� ���
print('\n�θ� �±� ���')
child_tag = bs.find('img')
print(child_tag.parent)

############################################################################
""" find_parent() �Լ��� find_parents() �Լ� """
############################################################################

# �ڱ��� �θ� �� �ϳ��� ã��.
p_tag = bs.find('p')
print('\n�ڱ��� �θ� �� �ϳ��� ã��.')
print(p_tag.find_parent('body')) # find�� ���� ���̴� ����.

# �θ� ��� ã��.
p_tag = bs.find('p')
print('\n�ڱ��� �θ� ��θ� ã��.')
parents = p_tag.find_parents()
for parent in parents:
    print(parent.name)