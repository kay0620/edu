import random

op = ['+','-','*','/']
correct = 0
wrong = 0

for i in range(1,6):
    nums = random.sample(range(1,30),2)
    opcho = random.choice(op)

    print('문제{} : {} {} {} '.format(i,nums[0], opcho, nums[1]))

    user = int(input('= '))

    answer = 0
    if opcho == '+':
        answer = sum(nums)
    elif opcho == '-':
        answer = nums[0] - nums[1]
    elif opcho == '*':
        answer = nums[0] * nums[1]
    elif opcho == '/':
        answer = nums[0] // nums[1]

    #print('정답: ' , answer)
    if answer == user:
        print('correct!')
        correct += 1
    else:
        print('wrong!')
        wrong += 1

print('정답 : {}개, 오답: {}개'.format(correct,wrong))
if correct == 5:
    print('Excellent!!')
