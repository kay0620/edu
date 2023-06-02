import random

print('--당첨자 발표--')

user = list(range(1,21))
random.shuffle(user)

chicken = random.sample(user,1)
remain_user = set(user) - set(chicken)
coffee = random.sample(list(remain_user),3)

print('치킨 당첨자 :', chicken)
print('커피 당첨자 :', coffee)

print(remain_user)
