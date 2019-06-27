"""urllib ���̺귯��"""
# urllib ���̺귯���� Python���� ���� ���õ� �����͸� ���� �̿��ϰ� �����ִ� ���̺귯��

# requst ���
import urllib.request # ���� ��� ������ �������� ���
req = urllib.request
d = req.urlopen("http://www.naver.com") # �������� �ҷ�����
status = d.getheaders()
for s in status:
    print(s)

# �� �������� ���� Ȯ��
print(d.status) # 200 �� ������� �ǹ�.

# �� �������� ������ �б�
print(d.read()) # html �ڵ� ���.

# parse ���
import urllib.parse # url�� �ѱ� �˻�� �Է��� �� �ֵ��� �����ִ� ���
def input_query():
    q = str(input("�˻�� �Է��ϼ���: ")) # �׳� �˻�
    return "&query=" + q

print(input_query()) # &query=�˻���

def input_query():
    q = urllib.parse.quote_plus(str(input("�˻�� �Է��ϼ���: "))) # ���ڵ��ؼ� �˻�(��ǻ�Ͱ� �˾Ƶ��� �� �ְ�)
    return "&query=" + q

print(input_query()) # &query=%EC%82%AC%EC%9A%A9%EC%95%88%ED%95%A8
print(urllib.parse.quote("�˻���")) # ������ %20���� ���ڵ�
print(urllib.parse.quote_plus("�˻���")) # ������ +�� ���ڵ�