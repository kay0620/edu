import random

print('UP & DOWN Game\n\n')

count = 10

#랜덤값을 생성
com = random.randint(1,100)


while count > 0:
    print('숫자를 입력하세요 (남은기회 {}번):'.format(count), end='')
    count -= 1
    
    #사용자가 입력한 값을 저장
    user = int(input())

    #두 값을 비교해서 UP or DOWN을 출력
    if user < com :
        print('UP')
    elif user > com:
        print('Down')
    else:
        print('\n\n축하합니다! 정답', '시도횟수 : {}번'.format(10-count) )
        break

if count == 0:
    print('Game Over! 정답은 ', com)
