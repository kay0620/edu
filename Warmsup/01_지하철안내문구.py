#3번 출력
for i in range(1,4):
    station = input(str(i) + '. 사용자입력:')
    print(station + '행 열차가 들어오고 있습니다')

#사용자가 종료할때까지
count = 0
while True:
    station = input('사용자 입력: ')    
    
    if station == '종료':
        print('프로그램을 종료합니다')
        break
    
    count += 1
    print(f'{count}. {station} 행 열차가 들어오고 있습니다')
