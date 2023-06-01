import random

print('--당첨자 발표--')

user = list(range(1,21))
random.shuffle(user)

winners = random.sample(user, 4)

print('치킨 당첨자 :', winners[0])
print('커피 당첨자 :', *winners[1:])
