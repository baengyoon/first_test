# 스터디모임 날짜정하기
from random import *

date = str(randint(4, 28))
print('오프라인 스터디 모임 날짜는 매월' + date + '일로 선정되었습니다.')

# 비밀번호 설정
url = 'http://naver.com'
my_str = url.replace('http://', '')
A = my_str.index('.')
my_str = my_str[:A]
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'

print(f'{url}의 비밀번호는{password}입니다.')

택시 승객 구하기
from random import *

cust = 0

for i in range(1, 50):
   time = randrange(5, 51)
   if 5 <= time <= 15:
       print('[O]', i + 1, '번째 손님 (소요시간 :', time, ' 분)')
       cust = cust + 1
   else:
       print('[ ]', i + 1, '번째 손님 (소요시간 :', time, ' 분)')

print('총 탑승승객 : ', cust, '분')

표준체중구하기
def std_weight(height, gender):
	if gender == 'M':
		print('키{0}cm 남자의 표준 체중은 {1}kg입니다.'. format(height, (height*height*22)/10000))
	else :
		print('키{0}cm 여자의 표준 체중은 {1}kg입니다.'. format(height, (height*height*21)/10000))

A = int(input('키를 입력하세요 : '))
B = input('성별을 입력하세요 : ')
std_weight(A, B)

score_file = open('score.txt', 'w', encoding = 'utf8')
print("수학 : 100", file = score_file)
score_file.close()

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
	def __init__(self, name, hp, damage):
		#Unit.__init__(self, name, hp)
		super().__init__(name, hp)
		self.damage = damage


	def attack(self, location):
		print('{0} : {1}방향으로 적군을 공격합니다. [공격력{2}]'\
					.format(self.name, location, self.damage))

	def damaged(self, damage):
		print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
		self.hp -= damage
		print('{0} : 현재 체력은{1} 입니다.'.format(self.name, self.hp))
		if self.hp <= 0:
			print('{0} : 파괴되었습니다.'.format(self.name))

firebat1 = AttackUnit('firebat', 50, 16)
firebat1.attack("8시")

firebat1.damaged(25)
firebat1.damaged(25)

class House:
	def __init__(self, location, house_type, deal_type, price, completion_year):
		self.location = location
		self.house_type = house_type
		self.deal_type = deal_type
		self.price = price
		self.completion_year = completion_year

	def show_detail(self):
		print('{0} {1} {2} {3} {4}'.format(self.location, self.house_type, \
					self.deal_type, self.price, self.completion_year))

house = []
A = House('강남', '아파트', '매매', '10억', '2010년')
B = House('마포', '오피스텔', '전세', '5억', '2007년')
C = House('송파', '빌라', '월세', '500/50', '2000년')

house.append(A)
house.append(B)
house.append(C)

print('총 {0}개의 매물이 있습니다.'.format(len(house)))
for i in house:
	i.show_detail()

try:
	print("나누기 전용 계산기입니다.")
	num1 = int(input("첫번째 숫자를 입력하시오 :"))
	num2 = int(input("두번째 숫자를 입력하시오 :"))
	print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError :
	print("에러! 잘못된 값을 입력했습니다.")

class SoldOutError(Exception):
	pass

chicken = 10
waiting = 1  # 홀 안에는 만석, 대기번호 1부터 시작

while (True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order < 1:
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError

	
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더이상 주문을 받지 않습니다.")
        break
