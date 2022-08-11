# 햄버거 주문

print('Welcome! Python Buger\n')

menu = ('올인원팩','투게더팩','트리오팩','패밀리팩')
price = [6000,7000,8000,10000]

#메뉴출력
print('주문할 콤보 번호와 수량 입력하세요')
for i,m in enumerate(menu):
    print(i+1,m)

#order,num = input('>> ').split()
#map에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환
order, num = map(int, input('>> ').split())

print(menu[order],num,'개 주문하셨습니다')
print('총 금액은 {}원 입니다'.format(price[order-1] * num))
