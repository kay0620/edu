import random


op_list = ['+','-','*','/']
correct = 0
wrong = 0


for i in range(5):
    # 1`. 숫자 2개 랜덤하게 생성
    n1= random.randint(1,30)
    n2= random.randint(1,30) #두개의 랜덤값이 중복이 될수도 ...

    # n1, n2 = random.sample(range(1,31),2) #두개의 값이 중복 안되게
    # print(n1, n2)

    # 2. 연산자 랜덤하게 생성
    
    op = random.choice(op_list)
    
    # 3. 문제 출력
    print('%d. %3d %s %3d = ' %(i+1, n1, op, n2) , end='')
    
    # 4. 사용자가 정답 입력
    user = int(input())
    
    
    # 5. 정답 확인    
    if op == '+':
        answer = n1 + n2
    elif op == '-':
        answer = n1 - n2
    elif op == '*':
        answer = n1 * n2
    elif op == '/':
        answer = n1 // n2
    else:
        answer = 0
    
    print('정답 : ', answer)
    
    # 6. 채점
    if answer == user:
        print('정답입니다')
        correct += 1
    else:
        print('땡! 틀렸습니다')
        wrong += 1
        
print(f'정답 : {correct}개, 오답 : {wrong}개')
if correct == 5:
    print('최고에요! 만점입니다! ')
