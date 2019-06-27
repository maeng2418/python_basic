"""정규식"""
"""
* 임의의 한문자가 존재
? 바로 앞의 문자가 존재하거나 존재하지 않음
* 바로 앞의 문자가 존재하지 않거나 무한대로 존재
+ 바로 앞의 문자가 한번 이상 존재
^ 바로 뒤의 문자로 문자열이 시작
$ 바로 앞의 문자로 문자열이 끝남
{숫자} 숫자만큼 반복
{숫자,} 숫자 이상만큼 반복
{숫자1, 숫자2} 숫자 1이상, 숫자 2 이하 만큼 반복
(문자열) 문자나 문자열을 묶음
[문자1, 문자2...] 대괄호 안에 있는 문자들이 존재하는지 검색
[^ ] ^기호 바로 뒤에 문자가 존재하지 않음
[:alpha:] 알파벳만 검색
[:alnum:] 알파벳, 숫자만 검색
[:digit:] 숫자만 검색
[:upper:] 대문자만 검색
\\ 역슬래쉬 글자 자체를 검색
\d 모든 숫자를 검색. [0-9]와 동일
\D 숫자를 제외한 모든 문자를 검색
\s 공백을 검색
\S 공백이 아닌 문자를 검색
\w 숫자 또는 문자를 검색 [a-zA-Z0-9]
\W 숫자 또는 문자가 아닌것을 검색
"""

# Q1
import re
r = re.compile("[ab]") # 찾고 싶은 글자지정 a나 b // 우리가 아는 글자나 패턴을 python이 아는 글자로 변환
print("\nBasic1 입니다.")
print(r.search("pizza")) # 해당 패턴이 하나라도 나오면 결과 출력
print(r.match("pizza")) # 정확한 글자만 출력
print(r.match("a"))

# Q2
print("\nBasic2 입니다.")
print(re.search("[ab]","pizza"))
print(re.match("[ab]","ab"))

# . - 임의의 한 문자 검색
print("\n. - 임의의 한 문자 검색")
print(re.search("a.c", "abc")) # catch
print(re.search("a.c", "afc")) # catch
print(re.search("a.c", "ac")) # none

# ? - 앞의 글자가 1개 또는 0개 그리고 바로 뒤에 글자 반드시 존재
print("\n? - 앞의 글자가 1개 또는 0개 그리고 바로 뒤에 글자 반드시 존재")
print(re.search("ck?w", "cw")) # catch
print(re.search("ck?w", "ckw")) # catch
print(re.search("ck?w", "ckkw")) # none //k가 하나더...
print(re.search("ck?w", "ckk")) # none
print(re.search("ck?w", "kkkw")) # none

# * - 바로 앞의 문자가 0개 또는 여러 개 그리고 바로 뒤에 글자 반드시 존재
print("\n* - 바로 앞의 문자가 0개 또는 여러 개 그리고 바로 뒤에 글자 반드시 존재")
print(re.search("ck*w", "cw")) # catch
print(re.search("ck*w", "ckw")) # catch
print(re.search("ck*w", "ckkw")) # catch
print(re.search("ck*w", "ckk")) # none
print(re.search("ck*w", "kkkw")) # none

# + - 바로 앞의 문자가 하나 이상 존재 그리고 바로 뒤에 글자 반드시 존재
print("\n+ -바로 앞의 문자가 한번 이상 존재")
print(re.search("ck+w", "ckw")) # catch
print(re.search("ck+w", "ckkkkkkkw")) # catch
print(re.search("ck+w", "ckkkkk")) # none
print(re.search("ck+w", "cw")) # none

# ^ - 시작문자 지정
print("\n^ - 시작문자 지정")
print(re.search("^c", "ckw")) # catch
print(re.search("^c", "sjw")) # none

# $ - 끝문자 지정
print("\n$ - 끝문자 지정")
print(re.search("e$", "apple")) # catch
print(re.search("e$", "banana")) # none

# [문자1, 문자2...] - 대괄호 안에 있는 문자들이 존재하는지 검색
print("\n[문자1, 문자2...] - 대괄호 안에 있는 문자들이 존재하는지 검색")
print(re.search("[abcd]", "pizza")) # catch
print(re.search("[abcd]", "bread")) # catch
print(re.search("[abcd]", "gefqs")) # none

# [^문자1, 문자2...] - ^ 기호 뒤에 문자들을 제외한 모든 문자 검색
print("\n[^문자1, 문자2...] - ^ 기호 뒤에 문자들을 제외한 모든 문자 검색")
print(re.search("[^ap]", "apple")) # catch 'l'
print(re.search("[^ab]", "bread")) # catch 'r'
print(re.search("[^ab]", "orange")) # catch 'o'

# - - 패턴이 연속적으로 여러가지가 있을 경우
print("\n- - 패턴이 연속적으로 여러가지가 있을 경우")
print(re.search("[a-g]", "apple")) # catch 'a'
print(re.search("[0-5]", "123678")) # catch '1'
print(re.search("[가-사]", "강원도에서")) # catch '강'

# search()함수 - 문자열 전체에서 정규식에 부합하는지 문자열이 있는지 검색
print("\nsearch()함수 - 문자열 전체에서 정규식에 부합하는지 문자열이 있는지 검색")
print(re.search("\d+", "서진수는 1975년에 태어 났습니다.")) # catch 1975

# match()함수 - 문자열의 처음이 정규식과 부합하는지 검색
print("\nmatch()함수 - 문자열의 처음이 정규식과 부합하는지 검색")
print(re.match("\d+", "서진수는 1975년에 태어 났습니다.")) # None
print(re.match("\d+", "1975년에 서진수는 태어 났습니다.")) # catch 1975

# findall()함수 - 정규식에 부합하는 모든 문자열을 리스트로 리턴
print("\nfindall()함수 - 정규식에 부합하는 모든 문자열을 리스트로 리턴")
print(re.findall("\d+", "서진수는 1975년 10월 23일 입니다 ^^")) # catch ['1975', '10', '23']

# split()함수 - 주어진 문자열을 특정 패턴을 기준으로 분리함
print("\nsplit()함수 - 주어진 문자열을 특정 패턴을 기준으로 분리함")
print(re.split("[:]+", "Apple Orange : Grape Cherry")) # catch ['Apple Orange ', ' Grape Cherry']
print(re.split("[: ]+", "Apple Orange : Grape Cherry")) # catch ['Apple', 'Orange', 'Grape', 'Cherry']

# sub()함수 - 주어진 패턴과 일치하는 문자를 변경함.
print("\nsub()함수 - 주어진 패턴과 일치하는 문자를 변경함.")
print(re.sub('-', '**', '751023-1901813')) # change to 751023**1901813
