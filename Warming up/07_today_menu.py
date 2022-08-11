#오늘 날짜 출력
from datetime import datetime

ttime = datetime.today()

print('='*20)
today = str(ttime.year) + '년' + str(ttime.month) + '월' + str(ttime.day) + '일'
print(today.center(20 - 3))
print('오늘의 메뉴'.center(15))

dinner = random.choice(menu)
print(dinner.center(15))
print('='*20)
