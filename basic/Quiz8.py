# Quiz) 주어진 코드를 활영하여 부동한 프로그램을 작성하시오.add()
# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2018년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    # 매물 정보 표시
    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")

house = []
a = House("강남", "아파트", "매매", "10억", "2018년")
b = House("마포", "오피스텔", "전세", "5억", "2007년")
c = House("송파", "빌라", "월세", "500/50", "2000년")

house.append(a)
house.append(b)
house.append(c)

print(f"총 {len(house)}대의 매물이 있습니다")
for i in house:
    i.show_detail()