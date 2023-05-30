print('Welcome! Python Buger\n')

menu= ['올인원팩','투게더팩','트리오팩','패밀리팩']
price = [6000,7000,8000,1000]

for n in range(len(menu)):
    print('%d. %s (%d원)'%(n+1, menu[n], price[n]))
    
order, num = map(int, input(">> ").split(' '))

order -= 1
print(menu[order], '을', num , '개 주문하셨습니다')
print('결제하실 금액은 ', price[order] * num , '원 입니다')
