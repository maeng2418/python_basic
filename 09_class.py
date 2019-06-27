"""클래스"""
# 클래스는 양식과 같은 형식이다 기본 샘플을 만들어놓고 필요할때마다 복사해 내용만 바꾸어서 사용한다.
# 변수나 함수를 모아놓은 집합
class bread:
    meterial = "팥"

first_bread = bread()
print(first_bread.meterial)

second_bread = bread()
second_bread.meterial = '슈크림'
print(second_bread.meterial)

# 클래스 안에 함수
class ramen:
    flavor = "매운맛"
    def say(self): # self는 인스턴스 자기 자신을 가리킨다.(클래스안에 함수 생성시 꼭 필요.)
        print("저는 %s입니다." %self.flavor)

first_ramen = ramen()
first_ramen.say()

# 생성자 (인스턴스 생성과 동시에 지정)
class americano:
    def __init__(self, m):
        self.meterial = m
    def say(self):
        print("저는 %s 아메리카노" %self.meterial)

first_americano = americano("Hot")
first_americano.say()

# 상속
class human:
    def __init__(self, name):
        self.name = name
    def intro(self):
        print("제 이름은 %s 입니다." %self.name)

class child(human): # child클래스는 human클래스 상속
    def hello(self):
        print("저는 %s 2세 입니다." %self.name)

adult = human("Kim")
adult.intro()
baby = child("Lee")
baby.intro()
baby.hello()