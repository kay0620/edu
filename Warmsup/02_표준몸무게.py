height = float(input('키: '))
weight = float(input('몸무게: '))
gender = input('성별: (남 or 여)')

bmi = weight / ((height*0.01)*(height*0.01))
print('BMI : %.2f' % bmi)

if gender == '남':
    if bmi < 18.5 :
        print('저체중')
    elif bmi < 25 :
        print('보통')
    elif bmi < 30:
        print('과체중')
    elif bmi <35:
        print('비만')
    else:
        print('초고도비만')
elif gender == '여':
    if bmi < 18.5 :
        print('저체중')
    elif bmi < 23 :
        print('보통')
    elif bmi < 25:
        print('과체중')
    elif bmi <30:
        print('비만')
    else:
        print('초고도비만')  
