import random

# 1. 로또 번호 출력

print('이번주 로또 결과')
winning_numbers = random.sample(range(1,46),6)
print(winning_numbers)
print()
my_lotto = random.sample(range(1,46),6)
print('나의 로또번호')
print(my_lotto)

# 2. 당첨 결과
print()
result = set(winning_numbers) & set(my_lotto)


# 3. 순위
rank = [6,6,5,4,3,2,1]
index = len(result)

#4. 당첨금
money = [0,0,5000,50000,1000000,50000000,1000000000]


# 5. 결과 출력
if index >= 2:
    print(f'축하합니다 {rank[index]}등 입니다')
    print(f'당첨금 : {money[index]}원 입니다')
else:
    print('아쉬워요! 다음에는 행운을 빌어요')

