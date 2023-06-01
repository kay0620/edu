print('='*20)
print('UP & DOWN Game'.center(20))
print('='*20)

maxnum = 100
score = maxnum

while True:
    print('1. Game Start')
    print('2. Game Score')
    print('3. End Game')
    menu = int(input('>> '))
    
    if menu == 1:
        print('Game Start')
        #랜덤값을 생성
        com = random.randint(1,maxnum + 1)
        
        count = 0

        while True:
            user = int(input(f'숫자를 입력하세요: '))
            count += 1

            #두 값을 비교해서 UP or DOWN을 출력
            if user < com:
                print('UP')
            elif user > com:
                print('DOWN')
            else:
                print(f'축하합니다! 정답입니다 (시도횟수 {count}번)')
                if score > count : 
                    print('기록갱신!')
                    score = count
                break
            
            
    elif menu == 2:
        print('Game Score')
        print('당신의 최고기록은 {}번 입니다'.format(score))
    elif menu == 3:
        print('게임 종료합니다')
        break
