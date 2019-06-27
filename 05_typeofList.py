"""리스트 유형"""
list = [1, "안녕하십니까", 10] # 다른 언어처럼 배열이 하나의 데이터 유형으로 정의될 필요가 없다.

print("%d" %list[0])
print("%s" %list[1])
print("%f" %list[2])

# 데이터 추가하기
list.append("추가")
print(list[3])

# 중간에 삽입하기
print(list)
list.insert(1,"삽입")
print(list)

# 데이터 삭제하기
del list[0] # 인덱스로 삭제
print(list)
list.remove("추가") # 해당 값으로 삭제
print(list)

# 데이터 정렬하기
num = [1,3,2,5,4,6]
num.sort()
print(num)
num.reverse()
print(num)

alpha = ["a", "C", "b", "f", "D"] # 대문자 먼저 정렬
alpha.sort()
print(alpha)

# 데이터 위치 찾기
foods = ["짬뽕", "탕수육", "깐풍기", "짜장면"]
print(foods.index('깐풍기'))

# 리스트 안에 리스트
foods = ["짬뽕", "찜닭", ["파스타", "돈까스"]]
print(foods[2])
print(foods[2][1])
print(foods[2][0:1])

# 리스트 갯수
list = [1,2,3,4,5,[2,3,4,5,6]]
print(len(list))

# 튜플
"""튜플은 생성된 후에는 내용을 변경하는 것이 불가능하다 & 소괄호를 사용한다."""
tup = (1, "안녕하시렵니까?", 10)
print (tup[0])

# 딕셔너리
dictionary = {
    '참치' : "tuna",
    '김밥' : 'kimbap',
    '과일' : 'fruit'
}

print(dictionary['김밥'])

# 수정하기
dictionary['김밥'] = "No data"
print(dictionary['김밥'])

# 삭제하기
del dictionary['김밥']
# dictionary.remove('fruit') remove로 삭제 안됨. 
print(dictionary)

# 키 값 조회
print(dictionary.keys())
print(set(dictionary)) # 순수 키값만 가져옴

# 값 조회
print(dictionary.values())

# 초기화
dictionary.clear()
print(dictionary)

# 해당키가 있는지 없는지 조회
dictionary = {
    '참치' : "tuna",
    '김밥' : 'kimbap',
    '과일' : 'fruit'
}
print('밥' in dictionary)
print('참치' in dictionary)