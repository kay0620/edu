## ver 2
## 사용자가 종료를 선택하기 전까지 게임 계속 진행 (while)
## 종료가 되면 win, lose, same 횟수 출력

import random

win = 0
lose = 0
same = 0

#4. 사용자가 종료를 선택하기 전까지 게임 계속 진행 (while)
while True:

    # 1. 컴퓨터가 가위,바위,보 중에서 하나 선택
    game = ['가위','바위','보']
    com = random.choice(game)

    # 2. 사용자가 가위바위보중에서 선택
    user = input('가위, 바위, 보중에서 입력하세요(종료): ')
    
    if user == '종료':
        print('게임을 종료합니다.')
        break

    # 3. 결과 출력
    madewin = {'가위':'보', '바위':'가위','보':'바위'}

    if user in madewin.keys(): #사용자가 맞게 입력했다면
        print('컴퓨터는 ', com)
        if user == com :
            print('비겼습니다')
            same += 1
        elif madewin[user] == com:
            print('축하합니다 사용자가 이겼습니다')
            win += 1
        else:
            print('아쉬워요! 졌습니다')
            lose += 1
    else:
        print('잘못입력하였습니다')
        
    print()

# 5. 종료가 되면 win, lose, same 횟수 출력
print(f'{win}번 이겼어요, {lose}번 졌어요, {same}번 비겼어요')
