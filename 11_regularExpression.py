"""���Խ�"""
"""
* ������ �ѹ��ڰ� ����
? �ٷ� ���� ���ڰ� �����ϰų� �������� ����
* �ٷ� ���� ���ڰ� �������� �ʰų� ���Ѵ�� ����
+ �ٷ� ���� ���ڰ� �ѹ� �̻� ����
^ �ٷ� ���� ���ڷ� ���ڿ��� ����
$ �ٷ� ���� ���ڷ� ���ڿ��� ����
{����} ���ڸ�ŭ �ݺ�
{����,} ���� �̻�ŭ �ݺ�
{����1, ����2} ���� 1�̻�, ���� 2 ���� ��ŭ �ݺ�
(���ڿ�) ���ڳ� ���ڿ��� ����
[����1, ����2...] ���ȣ �ȿ� �ִ� ���ڵ��� �����ϴ��� �˻�
[^ ] ^��ȣ �ٷ� �ڿ� ���ڰ� �������� ����
[:alpha:] ���ĺ��� �˻�
[:alnum:] ���ĺ�, ���ڸ� �˻�
[:digit:] ���ڸ� �˻�
[:upper:] �빮�ڸ� �˻�
\\ �������� ���� ��ü�� �˻�
\d ��� ���ڸ� �˻�. [0-9]�� ����
\D ���ڸ� ������ ��� ���ڸ� �˻�
\s ������ �˻�
\S ������ �ƴ� ���ڸ� �˻�
\w ���� �Ǵ� ���ڸ� �˻� [a-zA-Z0-9]
\W ���� �Ǵ� ���ڰ� �ƴѰ��� �˻�
"""

# Q1
import re
r = re.compile("[ab]") # ã�� ���� �������� a�� b // �츮�� �ƴ� ���ڳ� ������ python�� �ƴ� ���ڷ� ��ȯ
print("\nBasic1 �Դϴ�.")
print(r.search("pizza")) # �ش� ������ �ϳ��� ������ ��� ���
print(r.match("pizza")) # ��Ȯ�� ���ڸ� ���
print(r.match("a"))

# Q2
print("\nBasic2 �Դϴ�.")
print(re.search("[ab]","pizza"))
print(re.match("[ab]","ab"))

# . - ������ �� ���� �˻�
print("\n. - ������ �� ���� �˻�")
print(re.search("a.c", "abc")) # catch
print(re.search("a.c", "afc")) # catch
print(re.search("a.c", "ac")) # none

# ? - ���� ���ڰ� 1�� �Ǵ� 0�� �׸��� �ٷ� �ڿ� ���� �ݵ�� ����
print("\n? - ���� ���ڰ� 1�� �Ǵ� 0�� �׸��� �ٷ� �ڿ� ���� �ݵ�� ����")
print(re.search("ck?w", "cw")) # catch
print(re.search("ck?w", "ckw")) # catch
print(re.search("ck?w", "ckkw")) # none //k�� �ϳ���...
print(re.search("ck?w", "ckk")) # none
print(re.search("ck?w", "kkkw")) # none

# * - �ٷ� ���� ���ڰ� 0�� �Ǵ� ���� �� �׸��� �ٷ� �ڿ� ���� �ݵ�� ����
print("\n* - �ٷ� ���� ���ڰ� 0�� �Ǵ� ���� �� �׸��� �ٷ� �ڿ� ���� �ݵ�� ����")
print(re.search("ck*w", "cw")) # catch
print(re.search("ck*w", "ckw")) # catch
print(re.search("ck*w", "ckkw")) # catch
print(re.search("ck*w", "ckk")) # none
print(re.search("ck*w", "kkkw")) # none

# + - �ٷ� ���� ���ڰ� �ϳ� �̻� ���� �׸��� �ٷ� �ڿ� ���� �ݵ�� ����
print("\n+ -�ٷ� ���� ���ڰ� �ѹ� �̻� ����")
print(re.search("ck+w", "ckw")) # catch
print(re.search("ck+w", "ckkkkkkkw")) # catch
print(re.search("ck+w", "ckkkkk")) # none
print(re.search("ck+w", "cw")) # none

# ^ - ���۹��� ����
print("\n^ - ���۹��� ����")
print(re.search("^c", "ckw")) # catch
print(re.search("^c", "sjw")) # none

# $ - ������ ����
print("\n$ - ������ ����")
print(re.search("e$", "apple")) # catch
print(re.search("e$", "banana")) # none

# [����1, ����2...] - ���ȣ �ȿ� �ִ� ���ڵ��� �����ϴ��� �˻�
print("\n[����1, ����2...] - ���ȣ �ȿ� �ִ� ���ڵ��� �����ϴ��� �˻�")
print(re.search("[abcd]", "pizza")) # catch
print(re.search("[abcd]", "bread")) # catch
print(re.search("[abcd]", "gefqs")) # none

# [^����1, ����2...] - ^ ��ȣ �ڿ� ���ڵ��� ������ ��� ���� �˻�
print("\n[^����1, ����2...] - ^ ��ȣ �ڿ� ���ڵ��� ������ ��� ���� �˻�")
print(re.search("[^ap]", "apple")) # catch 'l'
print(re.search("[^ab]", "bread")) # catch 'r'
print(re.search("[^ab]", "orange")) # catch 'o'

# - - ������ ���������� ���������� ���� ���
print("\n- - ������ ���������� ���������� ���� ���")
print(re.search("[a-g]", "apple")) # catch 'a'
print(re.search("[0-5]", "123678")) # catch '1'
print(re.search("[��-��]", "����������")) # catch '��'

# search()�Լ� - ���ڿ� ��ü���� ���ԽĿ� �����ϴ��� ���ڿ��� �ִ��� �˻�
print("\nsearch()�Լ� - ���ڿ� ��ü���� ���ԽĿ� �����ϴ��� ���ڿ��� �ִ��� �˻�")
print(re.search("\d+", "�������� 1975�⿡ �¾� �����ϴ�.")) # catch 1975

# match()�Լ� - ���ڿ��� ó���� ���Խİ� �����ϴ��� �˻�
print("\nmatch()�Լ� - ���ڿ��� ó���� ���Խİ� �����ϴ��� �˻�")
print(re.match("\d+", "�������� 1975�⿡ �¾� �����ϴ�.")) # None
print(re.match("\d+", "1975�⿡ �������� �¾� �����ϴ�.")) # catch 1975

# findall()�Լ� - ���ԽĿ� �����ϴ� ��� ���ڿ��� ����Ʈ�� ����
print("\nfindall()�Լ� - ���ԽĿ� �����ϴ� ��� ���ڿ��� ����Ʈ�� ����")
print(re.findall("\d+", "�������� 1975�� 10�� 23�� �Դϴ� ^^")) # catch ['1975', '10', '23']

# split()�Լ� - �־��� ���ڿ��� Ư�� ������ �������� �и���
print("\nsplit()�Լ� - �־��� ���ڿ��� Ư�� ������ �������� �и���")
print(re.split("[:]+", "Apple Orange : Grape Cherry")) # catch ['Apple Orange ', ' Grape Cherry']
print(re.split("[: ]+", "Apple Orange : Grape Cherry")) # catch ['Apple', 'Orange', 'Grape', 'Cherry']

# sub()�Լ� - �־��� ���ϰ� ��ġ�ϴ� ���ڸ� ������.
print("\nsub()�Լ� - �־��� ���ϰ� ��ġ�ϴ� ���ڸ� ������.")
print(re.sub('-', '**', '751023-1901813')) # change to 751023**1901813
