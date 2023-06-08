class House:
    #매물 초기화 : 위치, 건물종류, 매물종류, 가격, 준공연도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
        
    #매물 정보 표시
    def show_detail(self):
        print(self.location,self.house_type,self.deal_type,self.price,self.completion_year)
        
        
h1 = House('센텀','아파트','매매','10억','2010년')
h2 = House('서면','오피스텔','전세','5억','2007년')
h3 = House('부산대','빌라','월세','500/50','2000년')

h1.show_detail()
h2.show_detail()
h3.show_detail()

h = []

h.append(House('센텀','아파트','매매','10억','2010년'))
h.append(House('서면','오피스텔','전세','5억','2007년'))
h.append(House('부산대','빌라','월세','500/50','2000년'))

print('총 {}개의 매물이 있습니다'.format(len(h)))

for e in h:
    e.show_detail()
