import random

#랜덤값 구하기
random.random()
random.randint(1,100) # 랜덤 정수 int형 N을 반환(a<=N<=b)
random.randrange(1,100,2) #1~99까지 홀수만

L = [1,2,4,5,6,9]
random.choice(L) #리스트에서 랜덤값
random.shuffle(L) #리스트를 섞어줌
random.sample(L,2)

mylist = ['가위','바위','보']
print(random.choice(mylist))


# 12개 띠 중에서 랜덤으로 3개 출력
li=['원숭이','닭','개','돼지','쥐','소','호랑이','토끼','용','뱀','말','양']
print(random.sample(li,3))

for i in range(3):
    print(random.choice(li))
