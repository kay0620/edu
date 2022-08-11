import random

game = ['','가위','바위','보']
madewin = {'가위':'보',
          '바위':'가위',
          '보':'바위'}

print('='*40)
print(*game)
print('='*40)

win = 0
lose = 0
same = 0

while True:
    user = int(input('\n1:가위, 2:바위, 3:보, 0:종료 중 하나 선택 >>'))
    com = random.choice(game[1:])   
    
    if user == 0:
        print('\n게임을 종료합니다')
        break
    
    user = game[user]
    print('User: {} vs Computer: {}'.format(user,com))
    
    if user == com:
        print('비겼습니다')
        same += 1
    elif madewin[user] == com:
        print('축하합니다! 이겼습니다')
        win += 1
    else:
        print('아쉬워요 졌습니다')
        lose += 1

#result
print('='*40)
print('win:{}, lose:{}, same:{}'.format(win,lose,same))
print('='*40)
