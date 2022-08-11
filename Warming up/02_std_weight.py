#표준몸무게 구하기
#표준 몸무게  = (키-100) * 0.9

height = float(input('키는 ? '))
stdweight = (height-100) * 0.9
print('당신의 표준 몸무게는 %.2f kg 입니다'%stdweight)
