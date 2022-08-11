import random

def rankint(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    money = [0,0,5000,50000,1000000,50000000,1000000000]
    
    c = lottos.count(0)
    m = len(set(win_nums) & set(lottos))
    
    return rank[m],money[m]

lotto=sorted(random.sample(range(1,46),6))
winning_number = sorted([31, 10, 45, 1, 6, 19])

print('이번주 로또 결과')
print(*winning_number)
print('나의 로또 번호')
print(*lotto)

result,winnings = rankint(lotto, winning_number)
if result < 6:
    print('축하해요!')
    print('{} 등 {}원 당첨'.format(result, winnings))
else:
    print('아쉬워요! 다음에는 행운을 빌어요!')
