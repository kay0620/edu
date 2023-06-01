import random

menu = ['김치찌개','된장찌개','떡볶이','파스타','치킨','피자','칼국수','밀면']
lunch, dinner = random.sample(menu,2)
print('오늘의 점심은 ', lunch)
print('오늘의 저녁은 ', dinner)


#가운데 정렬
import time, random

menu=['된장찌개','고추장찌개','불고기덥밥','칼국수','스파게티', '밀면']
print('='*25)
print(f'{time.strftime("%Y년%m월%d일"):^20}')
print(f'{"오늘의 메뉴":^20}')
print(f'{random.choice(menu):^20}')
print('='*25)


#한글 가운데 정렬

#한글 글자수
def korean_count(text):
    count = 0
    for char in text:
        if char.isalpha() and '가' <= char <= '힣':
            count += 1
        
    return count
  

import time , random

menu = ['김치찌개','된장찌개','떡볶이','파스타','치킨','피자','칼국수','밀면']

today = time.strftime("%Y년%m월%d일")
title = "오늘의 메뉴"
menu = random.choice(menu)
width = 40

print('='*width)
print(today.center(width-korean_count(today)))
print(title.center(width-korean_count(title)))
print(menu.center(width-korean_count(menu)))
print('='*width)
